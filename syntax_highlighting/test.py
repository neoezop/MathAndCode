import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from syntax_highlighting import syntax


class CustomMainWindow(QMainWindow):
    def __init__(self):
        super(CustomMainWindow, self).__init__()

        # Window setup
        # --------------

        # 1. Define the geometry of the main window
        self.setGeometry(300, 300, 800, 400)
        self.setWindowTitle("QScintilla Test")

        # 2. Create frame and layout
        self.__frm = QFrame(self)
        self.__frm.setStyleSheet("QWidget { background-color: #ffeaeaea }")
        self.__lyt = QVBoxLayout()
        self.__frm.setLayout(self.__lyt)
        self.setCentralWidget(self.__frm)
        self.__myFont = QFont()
        self.__myFont.setPointSize(14)

        # 3. Place a button
        self.__btn = QPushButton("Qsci")
        self.__btn.setFixedWidth(50)
        self.__btn.setFixedHeight(50)
        self.__btn.clicked.connect(self.__btn_action)
        self.__btn.setFont(self.__myFont)
        self.__lyt.addWidget(self.__btn)
        self.__editor = QPlainTextEdit()
        highlight = syntax.PythonHighlighter(self.__editor.document())
        infile = open('syntax.py', 'r')
        self.__editor.setPlainText(infile.read())
        self.__lyt.addWidget(self.__editor)
        self.show()

    ''''''

    def __btn_action(self):
        text = self.__editor.toPlainText()
        self.__editor.clear()
        highlight = syntax.PythonHighlighter(self.__editor.document())
        self.__editor.setPlainText(text)
        print("Hello World!")

    ''''''


''' End Class '''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myGUI = CustomMainWindow()

    sys.exit(app.exec_())

''''''
