# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calcu.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(700, 500)
        mainWindow.setMaximumSize(QtCore.QSize(700, 500))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.num_1 = QtWidgets.QPushButton(self.centralwidget)
        self.num_1.setMinimumSize(QtCore.QSize(60, 50))
        self.num_1.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.num_1.setFont(font)
        self.num_1.setObjectName("num_1")
        self.gridLayout.addWidget(self.num_1, 2, 0, 1, 1)
        self.num_4 = QtWidgets.QPushButton(self.centralwidget)
        self.num_4.setMinimumSize(QtCore.QSize(60, 50))
        self.num_4.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.num_4.setFont(font)
        self.num_4.setObjectName("num_4")
        self.gridLayout.addWidget(self.num_4, 2, 3, 1, 1)
        self.num_5 = QtWidgets.QPushButton(self.centralwidget)
        self.num_5.setMinimumSize(QtCore.QSize(60, 50))
        self.num_5.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.num_5.setFont(font)
        self.num_5.setObjectName("num_5")
        self.gridLayout.addWidget(self.num_5, 2, 4, 1, 1)
        self.subtract = QtWidgets.QPushButton(self.centralwidget)
        self.subtract.setMinimumSize(QtCore.QSize(60, 50))
        self.subtract.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.subtract.setFont(font)
        self.subtract.setObjectName("subtract")
        self.gridLayout.addWidget(self.subtract, 3, 7, 1, 1)
        self.undo = QtWidgets.QPushButton(self.centralwidget)
        self.undo.setMinimumSize(QtCore.QSize(60, 50))
        self.undo.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.undo.setFont(font)
        self.undo.setObjectName("undo")
        self.gridLayout.addWidget(self.undo, 2, 6, 1, 1)
        self.decimal_point = QtWidgets.QPushButton(self.centralwidget)
        self.decimal_point.setMinimumSize(QtCore.QSize(60, 50))
        self.decimal_point.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.decimal_point.setFont(font)
        self.decimal_point.setObjectName("decimal_point")
        self.gridLayout.addWidget(self.decimal_point, 4, 4, 1, 1)
        self.percent = QtWidgets.QPushButton(self.centralwidget)
        self.percent.setMinimumSize(QtCore.QSize(60, 50))
        self.percent.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.percent.setFont(font)
        self.percent.setObjectName("percent")
        self.gridLayout.addWidget(self.percent, 4, 2, 1, 1)
        self.sqaure_root = QtWidgets.QPushButton(self.centralwidget)
        self.sqaure_root.setMinimumSize(QtCore.QSize(60, 50))
        self.sqaure_root.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sqaure_root.setFont(font)
        self.sqaure_root.setObjectName("sqaure_root")
        self.gridLayout.addWidget(self.sqaure_root, 4, 5, 1, 1)
        self.num_9 = QtWidgets.QPushButton(self.centralwidget)
        self.num_9.setMinimumSize(QtCore.QSize(60, 50))
        self.num_9.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.num_9.setFont(font)
        self.num_9.setObjectName("num_9")
        self.gridLayout.addWidget(self.num_9, 3, 3, 1, 1)
        self.num_3 = QtWidgets.QPushButton(self.centralwidget)
        self.num_3.setMinimumSize(QtCore.QSize(60, 50))
        self.num_3.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.num_3.setFont(font)
        self.num_3.setObjectName("num_3")
        self.gridLayout.addWidget(self.num_3, 2, 2, 1, 1)
        self.answer_edit = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.answer_edit.setFont(font)
        self.answer_edit.setReadOnly(True)
        self.answer_edit.setObjectName("answer_edit")
        self.gridLayout.addWidget(self.answer_edit, 0, 0, 1, 9)
        self.backspace = QtWidgets.QPushButton(self.centralwidget)
        self.backspace.setMinimumSize(QtCore.QSize(60, 50))
        self.backspace.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.backspace.setFont(font)
        self.backspace.setObjectName("backspace")
        self.gridLayout.addWidget(self.backspace, 2, 7, 1, 1)
        self.redo = QtWidgets.QPushButton(self.centralwidget)
        self.redo.setMinimumSize(QtCore.QSize(60, 50))
        self.redo.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.redo.setFont(font)
        self.redo.setObjectName("redo")
        self.gridLayout.addWidget(self.redo, 2, 5, 1, 1)
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setMinimumSize(QtCore.QSize(60, 50))
        self.clear.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.gridLayout.addWidget(self.clear, 2, 8, 1, 1)
        self.exponent = QtWidgets.QPushButton(self.centralwidget)
        self.exponent.setMinimumSize(QtCore.QSize(60, 50))
        self.exponent.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.exponent.setFont(font)
        self.exponent.setObjectName("exponent")
        self.gridLayout.addWidget(self.exponent, 4, 3, 1, 1)
        self.num_7 = QtWidgets.QPushButton(self.centralwidget)
        self.num_7.setMinimumSize(QtCore.QSize(60, 50))
        self.num_7.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.num_7.setFont(font)
        self.num_7.setObjectName("num_7")
        self.gridLayout.addWidget(self.num_7, 3, 1, 1, 1)
        self.num_2 = QtWidgets.QPushButton(self.centralwidget)
        self.num_2.setMinimumSize(QtCore.QSize(60, 50))
        self.num_2.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.num_2.setFont(font)
        self.num_2.setObjectName("num_2")
        self.gridLayout.addWidget(self.num_2, 2, 1, 1, 1)
        self.equals = QtWidgets.QPushButton(self.centralwidget)
        self.equals.setMinimumSize(QtCore.QSize(220, 50))
        self.equals.setMaximumSize(QtCore.QSize(220, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.equals.setFont(font)
        self.equals.setObjectName("equals")
        self.gridLayout.addWidget(self.equals, 4, 6, 1, 3)
        self.divide = QtWidgets.QPushButton(self.centralwidget)
        self.divide.setMinimumSize(QtCore.QSize(60, 50))
        self.divide.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.divide.setFont(font)
        self.divide.setObjectName("divide")
        self.gridLayout.addWidget(self.divide, 3, 6, 1, 1)
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setMinimumSize(QtCore.QSize(60, 50))
        self.add.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add.setFont(font)
        self.add.setObjectName("add")
        self.gridLayout.addWidget(self.add, 3, 8, 1, 1)
        self.ratio = QtWidgets.QPushButton(self.centralwidget)
        self.ratio.setMinimumSize(QtCore.QSize(130, 50))
        self.ratio.setMaximumSize(QtCore.QSize(130, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ratio.setFont(font)
        self.ratio.setObjectName("ratio")
        self.gridLayout.addWidget(self.ratio, 4, 0, 1, 2)
        self.multiply = QtWidgets.QPushButton(self.centralwidget)
        self.multiply.setMinimumSize(QtCore.QSize(60, 50))
        self.multiply.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.multiply.setFont(font)
        self.multiply.setObjectName("multiply")
        self.gridLayout.addWidget(self.multiply, 3, 5, 1, 1)
        self.num_8 = QtWidgets.QPushButton(self.centralwidget)
        self.num_8.setMinimumSize(QtCore.QSize(60, 50))
        self.num_8.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.num_8.setFont(font)
        self.num_8.setObjectName("num_8")
        self.gridLayout.addWidget(self.num_8, 3, 2, 1, 1)
        self.num_6 = QtWidgets.QPushButton(self.centralwidget)
        self.num_6.setMinimumSize(QtCore.QSize(60, 50))
        self.num_6.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.num_6.setFont(font)
        self.num_6.setObjectName("num_6")
        self.gridLayout.addWidget(self.num_6, 3, 0, 1, 1)
        self.num_0 = QtWidgets.QPushButton(self.centralwidget)
        self.num_0.setMinimumSize(QtCore.QSize(60, 50))
        self.num_0.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.num_0.setFont(font)
        self.num_0.setObjectName("num_0")
        self.gridLayout.addWidget(self.num_0, 3, 4, 1, 1)
        self.input_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.input_edit.setMaximumSize(QtCore.QSize(1000, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.input_edit.setFont(font)
        self.input_edit.setObjectName("input_edit")
        self.gridLayout.addWidget(self.input_edit, 1, 0, 1, 9)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.redo.clicked['bool'].connect(self.input_edit.redo)
        self.undo.clicked['bool'].connect(self.input_edit.undo)
        self.clear.clicked['bool'].connect(self.input_edit.clear)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "ChrisCalcu"))
        self.num_1.setText(_translate("mainWindow", "1"))
        self.num_4.setText(_translate("mainWindow", "4"))
        self.num_5.setText(_translate("mainWindow", "5"))
        self.subtract.setText(_translate("mainWindow", "-"))
        self.undo.setText(_translate("mainWindow", "undo"))
        self.decimal_point.setText(_translate("mainWindow", "."))
        self.percent.setText(_translate("mainWindow", "%"))
        self.sqaure_root.setText(_translate("mainWindow", "s"))
        self.num_9.setText(_translate("mainWindow", "9"))
        self.num_3.setText(_translate("mainWindow", "3"))
        self.backspace.setText(_translate("mainWindow", "B"))
        self.redo.setText(_translate("mainWindow", "redo"))
        self.clear.setText(_translate("mainWindow", "clear"))
        self.exponent.setText(_translate("mainWindow", "x^2"))
        self.num_7.setText(_translate("mainWindow", "7"))
        self.num_2.setText(_translate("mainWindow", "2"))
        self.equals.setText(_translate("mainWindow", "="))
        self.divide.setText(_translate("mainWindow", "/"))
        self.add.setText(_translate("mainWindow", "+"))
        self.ratio.setText(_translate("mainWindow", "2 : 8 = 9 : x"))
        self.multiply.setText(_translate("mainWindow", "*"))
        self.num_8.setText(_translate("mainWindow", "8"))
        self.num_6.setText(_translate("mainWindow", "6"))
        self.num_0.setText(_translate("mainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
