from sys import setprofile
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QTextCharFormat
from main_win_ui import Ui_mainWindow

class MainWin(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.connect_widget_to_action()

    def connect_widget_to_action(self):
        num_0 = self.ui.num_0.text()
        self.ui.num_0.clicked.connect(lambda:self.ui.input_edit.insertPlainText(num_0))

        num_1 = self.ui.num_1.text()
        self.ui.num_1.clicked.connect(lambda:self.ui.input_edit.insertPlainText(num_1))
        
        num_2 = self.ui.num_2.text()
        self.ui.num_2.clicked.connect(lambda:self.ui.input_edit.insertPlainText(num_2))

        num_3 = self.ui.num_3.text()
        self.ui.num_3.clicked.connect(lambda:self.ui.input_edit.insertPlainText(num_3))

        num_4 = self.ui.num_4.text()
        self.ui.num_4.clicked.connect(lambda:self.ui.input_edit.insertPlainText(num_4))

        num_5 = self.ui.num_5.text()
        self.ui.num_5.clicked.connect(lambda:self.ui.input_edit.insertPlainText(num_5))

        num_6 = self.ui.num_6.text()
        self.ui.num_6.clicked.connect(lambda:self.ui.input_edit.insertPlainText(num_6))
        
        num_7 = self.ui.num_7.text()
        self.ui.num_7.clicked.connect(lambda:self.ui.input_edit.insertPlainText(num_7))

        num_8 = self.ui.num_8.text()
        self.ui.num_8.clicked.connect(lambda:self.ui.input_edit.insertPlainText(num_8))

        num_9 = self.ui.num_9.text()
        self.ui.num_9.clicked.connect(lambda:self.ui.input_edit.insertPlainText(num_9))

        multiply = self.ui.multiply.text()
        self.ui.multiply.clicked.connect(lambda:self.ui.input_edit.insertPlainText(' '+multiply+' '))

        divide = self.ui.divide.text()
        self.ui.divide.clicked.connect(lambda:self.ui.input_edit.insertPlainText(' '+divide+' '))

        subtract = self.ui.subtract.text()
        self.ui.subtract.clicked.connect(lambda:self.ui.input_edit.insertPlainText(' '+subtract+' '))

        add = self.ui.add.text()
        self.ui.add.clicked.connect(lambda:self.ui.input_edit.insertPlainText(' '+add+' '))

        percent_sign = self.ui.percent.text()
        self.ui.percent.clicked.connect(lambda:self.ui.input_edit.insertPlainText(percent_sign))

        self.ui.percent.clicked.connect(self.percent)

        decimal_point = self.ui.decimal_point.text()
        self.ui.decimal_point.clicked.connect(lambda:self.ui.input_edit.insertPlainText(decimal_point))

        self.ui.equals.clicked.connect(self.answer_func)
        self.ui.exponent.clicked.connect(self.exponent)
        # self.ui.sqaure_root.clicked.connect(self.percent)

    def answer_func(self):
        try:
            plainText = self.ui.input_edit.toPlainText()
            if plainText[-1].isdigit():
                plainAnswer = eval(plainText)
                print(plainAnswer)
                self.ui.answer_edit.setPlainText(plainText+' '+'='+' '+str(plainAnswer))
        except ZeroDivisionError:
            self.ui.answer_edit.setPlainText('Can\'t divide by zero')
        
        except IndexError:
            self.ui.answer_edit.setPlainText('Give me something to solve')

    def exponent(self):
        ftxt = self.ui.input_edit.currentCharFormat()
        alignment = ftxt.verticalAlignment()
        if alignment == QTextCharFormat.AlignNormal:
            ftxt.setVerticalAlignment(QTextCharFormat.AlignSuperScript)
            self.get_text_for_index = self.ui.input_edit.toPlainText()

            self.get_index = self.get_text_for_index.index(self.get_text_for_index[-1])

            print(self.get_index)
        else:
            ftxt.setVerticalAlignment(QTextCharFormat.AlignNormal)
            
            self.all = self.ui.input_edit.toPlainText()
            for index,value in enumerate(self.all):
                if index > self.get_index and index < len(self.all)+1:
                    self.exponent_answer = int(self.get_text_for_index[-1])**int(value)
                    print(self.exponent_answer)
        self.ui.input_edit.setCurrentCharFormat(ftxt)

    def percent(self):
        self.txt = self.ui.input_edit.toPlainText()
        self.txt = self.txt.split()
        for i in self.txt:
            if i.__contains__('%'):
                print(i)
                percent = int(i[:-1])/100
                print('Yeah '+str(percent))

    def sqaure_root(self):
        pass
    


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    main_window = MainWin()
    main_window.show()
    sys.exit(app.exec_())
