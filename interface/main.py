import re

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from converters.translator import *

# noinspection PyUnresolvedReferences
from interface import resource_rc


class Converter(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.__intRegex__ = re.compile(r"^[-]?\d+$")

    def isInt(self, s: str) -> bool:
        return self.__intRegex__.match(str(s)) is not None

    ##convertSignal = pyqtSignal(str, arguments=['convert'])
    convertResult = pyqtSignal(str, arguments=['convert'])
    countValueResult = pyqtSignal(str, arguments=['countValue'])

    # слот для расчета значения (вывода) рекурсий в точке
    @pyqtSlot(str, str, bool)
    def countValue(self, nRaw: str, inputText: str, isPythonToMath: bool):
        # todo вылетает если N большое (переполнение стека и тд)
        result = ""
        if not self.isInt(nRaw):
            result = "nNotIntError"
            # result.append("nNotIntError")
        else:
            # solve_res = "ТЕСТ"
            n = int(nRaw)
            filtered_lines = self.filterAndSplitMainInput(inputText)
            '''result.append("Код:\n" + "\n".join(filtered_lines))       # 1-й элемент массива - код'''
            if isPythonToMath:
                result = self.countValuePython(n, filtered_lines)
        print(result)
        self.countValueResult.emit(result)

    def countValuePython(self, n, filtered_lines):  # returns int value or print output (depends on ЕГЭ task)
        pyToMath = py_to_math()
        try:
            funcs = pyToMath.break_to_funcs(filtered_lines)
            result_arr = []
            for f in funcs:
                # print(ff.name)
                int_res = get_int_result_for(f"{f.name}({n})", pyToMath.code)  # todo fix lowercase
                str_res = get_str_result_for(f"{f.name}({n})", pyToMath.code)
                tmp = f"Функция: {f.name}({n})"
                if int_res is not None:
                    tmp = f"{tmp}\n{f.name}({n}) = {str(int_res)}"
                if str_res != "":
                    tmp = f"{tmp}\nВыведено на консоль: {str_res}"
                if int_res is None and str_res == "":
                    tmp = f"{tmp}\nФункция ничего не выводит и ничего не возвращает"
                result_arr.append(tmp)
            result = "\n\n".join(result_arr)
            print(result)

            '''pyToMath = py_to_math()
            pyToMath.break_to_funcs(filtered_lines)
            result = self.countForNpython(n, filtered_lines)
            print(get_int_result_for(f"f({n})", pyToMath.code))  # todo FIX works only for function named f !!!
            №inputText = self.convertMathToPy(filtered_lines)
            output=""
            #convertedText = py_to_math_converter.convert_py_to_math(py_to_math_converter, funcs)'''
        except BaseException as exception:  # todo is it needed????????
            print("solve for n error", exception)
            result = "PyBreakToFuncsError"
        return result

    # слот для перевода из одной формы в другую
    @pyqtSlot(str, bool)
    def convert(self, inputText: str, isPythonToMath: bool):
        filtered_lines = self.filterAndSplitMainInput(inputText)

        if isPythonToMath:
            convertedText = self.convertPyToMath(filtered_lines)
        else:
            # todo если вбить бред, мат. представление не вылетает, сделать, чтобы вылетало
            # todo пока вылет ошибки реализован при условии, что возвращается def f(n):
            convertedText = self.convertMathToPy(filtered_lines)
        print(convertedText)
        self.convertResult.emit(convertedText)

    def convertPyToMath(self, filtered_lines):
        pyToMath = py_to_math()
        try:
            funcs = pyToMath.break_to_funcs(filtered_lines)
            convertedText = py_to_math_converter.convert_py_to_math(py_to_math_converter, funcs)
        except BaseException as exception:
            print("convert error", exception)
            convertedText = "PyToMathError"  # todo python to math error dialog
        return convertedText

    def convertMathToPy(self, filtered_lines):
        mathToPy = math_to_py()
        try:
            funcs = mathToPy.break_to_funcs(filtered_lines)
            convertedText = math_to_py_converter.convert_math_to_py(math_to_py_converter, funcs)
            if convertedText == "def f(n):":  # todo remove this workaround later
                convertedText = "MathToPyError"
        except BaseException as exception:
            print("convert error", exception)
            convertedText = "MathToPyError"  # todo math to python error dialog
        return convertedText

    # Преобразование ввода Python-кода или мат. представления
    def filterAndSplitMainInput(self, inputText):
        lines = inputText.splitlines()
        filtered_lines = []
        for line in lines:
            if not (re.match(r'^([\s\t]+)$', line) or line == ''):
                filtered_lines.append(line)
        return filtered_lines


if __name__ == "__main__":
    import os
    import sys

    # создаём экземпляр приложения
    app = QGuiApplication(sys.argv)
    # app.setWindowIcon(QIcon(f"{os.path.sep}images{os.path.sep}demo_icon.png"))
    # создаём QML движок
    engine = QQmlApplicationEngine()
    # создаём объект калькулятора
    converter = Converter()
    # и регистрируем его в контексте QML
    engine.rootContext().setContextProperty("converter", converter)
    # загружаем файл qml в движок
    engine.load(os.path.join("layouts", "main.qml"))
    engine.quit.connect(app.quit)
    sys.exit(app.exec_())
