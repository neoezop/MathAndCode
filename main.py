import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog, QDialog, QMainWindow
from PyQt5.QtWidgets import QInputDialog

solve_for_n_ui, _ = uic.loadUiType("solve_for_n_window.ui")
history_ui, _ = uic.loadUiType("history_window.ui")
main_ui, _ = uic.loadUiType('main_window.ui')
help_ui, _ = uic.loadUiType('help_window.ui')
w = None

class MainWindow(QMainWindow, main_ui):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        button_history = self.findChild(QtWidgets.QPushButton, "buttonHistory")
        button_history.clicked.connect(self.show_history)

        button_translate = self.findChild(QtWidgets.QToolButton, "translateButton")
        button_save = self.findChild(QtWidgets.QPushButton, "buttonSave")
        button_help = self.findChild(QtWidgets.QPushButton, "buttonHelp")
        button_solve_for_n = self.findChild(QtWidgets.QPushButton, "buttonSolveForN")
        combo_box_type = self.findChild(QtWidgets.QComboBox, "comboBoxType")
        button_translate.clicked.connect(self.translate)
        button_save.clicked.connect(self.save)
        button_help.clicked.connect(self.show_help)
        button_solve_for_n.clicked.connect(self.solve_for_n)
        combo_box_type.currentIndexChanged.connect(self.change_input_type)

    def translate(self):
        print("translate")
        text_edit_input = self.findChild(QtWidgets.QTextEdit, "textEditInput")
        ls = text_edit_input.toPlainText().split('\n')
        print(ls)
        #print("input:"+ls)

    def save(self):
        print("show save menu and save")
        #todo export in file
        #QInputDialog.show()
        QFileDialog.getSaveFileName(self, 'Экспортировать в файл', '/home')

    def show_help(self):
        print("show help menu")
        w.setCurrentIndex(3)
        w.setWindowTitle("Помощь - Math and Code")

    def solve_for_n(self):
        print("solve for n")
        w.setCurrentIndex(2)
        w.setWindowTitle("Решить для N - Math and Code")

    def change_input_type(self, index):
        print("translate: %d", index)

    def show_history(self):
        print("show history")
        w.setCurrentIndex(1)
        w.setWindowTitle("История - Math and Code")


class HistoryWindow(QMainWindow, history_ui):
    def __init__(self, parent=None):
        super(HistoryWindow, self).__init__(parent)
        self.setupUi(self)
        button_back = self.findChild(QtWidgets.QPushButton, "buttonBack")
        button_back.clicked.connect(self.back)

    def back(self):
        print("back to main")
        w.setCurrentIndex(0)
        w.setWindowTitle("Главное меню - Math and Code")


class SolveForNWindow(QMainWindow, solve_for_n_ui):

    def __init__(self, parent=None):
        super(SolveForNWindow, self).__init__(parent)
        self.setupUi(self)
        button_back = self.findChild(QtWidgets.QPushButton, "buttonBack")
        button_back.clicked.connect(self.back)

    def back(self):
        print("back to main")
        w.setCurrentIndex(0)
        w.setWindowTitle("Главное меню - Math and Code")


class HelpWindow(QMainWindow, help_ui):

    def __init__(self, parent=None):
        super(HelpWindow, self).__init__(parent)
        self.setupUi(self)
        button_back = self.findChild(QtWidgets.QPushButton, "buttonBack")
        button_back.clicked.connect(self.back)

    def back(self):
        print("back to main")
        w.setCurrentIndex(0)
        w.setWindowTitle("Главное меню - Math and Code")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    w = QtWidgets.QStackedWidget()
    main_window = MainWindow()
    history_window = HistoryWindow()
    solve_for_n_window = SolveForNWindow()
    help_window = HelpWindow()
    w.addWidget(main_window)
    w.addWidget(history_window)
    w.addWidget(solve_for_n_window)
    w.addWidget(help_window)
    w.resize(640, 407)
    w.setWindowTitle("Главное меню - Math and Code")
    w.show()
    sys.exit(app.exec_())



