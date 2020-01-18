from PyQt5 import QtGui
from PyQt5.Qsci import QsciLexerPython
from PyQt5.QtGui import QColor, QFont


class PythonLexer(QsciLexerPython):
    # todo !!! FINISH ALL LEXER COLORS AND SIZES (SET DEF VALUES)
    def __init__(self, parent):
        super(PythonLexer, self).__init__(parent)
        # Default text settings
        # ----------------------
        self.setDefaultColor(QColor("#000000"))
        self.setDefaultPaper(QColor("#ffffff"))
        self.setDefaultFont(QFont("Open Sans", 30))

        # Initialize colors per style
        # ----------------------------
        # todo where is 0 id
        '''self.setColor(QColor("#557F5F"), 1)  # comments
        self.setColor(QColor("#FF0000"), 2)  # numbers
        self.setColor(QColor("#0000C0"), 3)  # strings
        self.setColor(QColor("#7F0055"), 5)  # keywords
        # todo where are 6 7 8 ?
        self.setColor(QColor("#006600"), 9)  # class names and other'''

        # Initialize paper colors per style
        # ----------------------------------
        '''self.setPaper(QColor("#F0F0f0"), 1)  # comments
        self.setPaper(QColor("#F0F0f0"), 2)  # numbers
        self.setPaper(QColor("#F0F0f0"), 3)  # strings
        self.setPaper(QColor("#F0F0f0"), 5)  # keywords
        self.setPaper(QColor("#F0F0f0"), 9)  # class names and other'''

        # Initialize fonts per style
        # ---------------------------
        self.setFont(QFont("Open Sans", 30), 0)  # default
        self.setFont(QFont("Open Sans", 30, italic=True), 1)  # comments
        self.setFont(QFont("Open Sans", 30), 2)  # numbers
        self.setFont(QFont("Open Sans", 30), 3)  # strings
        self.setFont(QFont("Open Sans", 30), 4)

        self.setFont(QFont("Open Sans", 30, weight=QtGui.QFont.Bold), 5)  # keywords
        self.setFont(QFont("Open Sans", 30, weight=QtGui.QFont.Bold), 8)  # class name
        self.setFont(QFont("Open Sans", 30, weight=QtGui.QFont.Bold), 9)  # method name
        self.setFont(QFont("Open Sans", 30), 13)  # unclosed string
