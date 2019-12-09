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

    ##convertSignal = pyqtSignal(str, arguments=['convert'])
    convertResult = pyqtSignal(str, arguments=['convert'])

    # слот для перевода из одной формы в другую
    @pyqtSlot(str, bool)
    def convert(self, inputText: str, isPythonToMath):
        lines = inputText.splitlines()
        filtered_lines = []
        for line in lines:
            if not (re.match(r'^([\s\t\n]+)$', line) or line == ''):
                filtered_lines.append(line)

        if (isPythonToMath):
            pyToMath = py_to_math()
            funcs = pyToMath.break_to_funcs(filtered_lines)
            convertedText = py_to_math_converter.convert_py_to_math(py_to_math_converter, funcs)
        else:
            mathToPy = math_to_py()
            funcs = mathToPy.break_to_funcs(inputText.splitlines())
            convertedText = math_to_py_converter.convert_math_to_py(math_to_py_converter, funcs)
        print(convertedText)
        self.convertResult.emit(convertedText)


if __name__ == "__main__":
    import os
    import sys

    # создаём экземпляр приложения
    app = QGuiApplication(sys.argv)
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
