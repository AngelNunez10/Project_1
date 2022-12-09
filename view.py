# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 500)
        MainWindow.setMinimumSize(QtCore.QSize(400, 500))
        MainWindow.setMaximumSize(QtCore.QSize(400, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tab_3 = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_3.setGeometry(QtCore.QRect(0, 0, 411, 481))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tab_3.setFont(font)
        self.tab_3.setObjectName("tab_3")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.input_num = QtWidgets.QLineEdit(self.tab)
        self.input_num.setGeometry(QtCore.QRect(210, 60, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.input_num.setFont(font)
        self.input_num.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.input_num.setObjectName("input_num")
        self.label_num = QtWidgets.QLabel(self.tab)
        self.label_num.setGeometry(QtCore.QRect(60, 50, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_num.setFont(font)
        self.label_num.setObjectName("label_num")
        self.input_amount = QtWidgets.QLineEdit(self.tab)
        self.input_amount.setGeometry(QtCore.QRect(150, 110, 121, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.input_amount.setFont(font)
        self.input_amount.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.input_amount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.input_amount.setObjectName("input_amount")
        self.radio_withdraw = QtWidgets.QRadioButton(self.tab)
        self.radio_withdraw.setGeometry(QtCore.QRect(170, 140, 82, 31))
        self.radio_withdraw.setObjectName("radio_withdraw")
        self.label_amount = QtWidgets.QLabel(self.tab)
        self.label_amount.setGeometry(QtCore.QRect(60, 90, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_amount.setFont(font)
        self.label_amount.setObjectName("label_amount")
        self.radio_deposit = QtWidgets.QRadioButton(self.tab)
        self.radio_deposit.setGeometry(QtCore.QRect(70, 140, 91, 31))
        self.radio_deposit.setObjectName("radio_deposit")
        self.button_submit = QtWidgets.QPushButton(self.tab)
        self.button_submit.setGeometry(QtCore.QRect(130, 180, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_submit.setFont(font)
        self.button_submit.setObjectName("button_submit")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(120, -10, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.button_balance = QtWidgets.QPushButton(self.tab)
        self.button_balance.setGeometry(QtCore.QRect(130, 240, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_balance.setFont(font)
        self.button_balance.setObjectName("button_balance")
        self.label_output = QtWidgets.QLabel(self.tab)
        self.label_output.setGeometry(QtCore.QRect(10, 310, 351, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_output.setFont(font)
        self.label_output.setText("")
        self.label_output.setObjectName("label_output")
        self.tab_3.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_num.setText(_translate("MainWindow", "<html><head/><body><p>Account Number:</p></body></html>"))
        self.radio_withdraw.setText(_translate("MainWindow", "Withdraw"))
        self.label_amount.setText(_translate("MainWindow", "Amount:"))
        self.radio_deposit.setText(_translate("MainWindow", "Deposit"))
        self.button_submit.setText(_translate("MainWindow", "SUBMIT"))
        self.label.setText(_translate("MainWindow", "BANK ACCOUNT"))
        self.button_balance.setText(_translate("MainWindow", "Check Balance"))
        self.tab_3.setTabText(self.tab_3.indexOf(self.tab), _translate("MainWindow", "BANK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
