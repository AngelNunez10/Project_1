from PyQt5.QtWidgets import *
from view import *
from account import *

# pyuic5 -x view.ui -o view.py


QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

dict = dict()

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        """
        Constructor to set default values for an account object
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.radio_deposit.setChecked(True)

        self.button_submit.clicked.connect(lambda: self.submit())

        self.button_balance.clicked.connect(lambda: self.check_balance())



    def enter_account_num(self):
        """
        Method that creates an account or looks to see if an account already exist.

         """
        self.num = int(self.input_num.text().strip())


        if self.num in dict:
            self.account = Account(self.num)
            self.account.deposit(dict.get(self.num))
        else:
            self.account = Account(self.num)

        self.label_output.setText(f'Account Name: {self.account.get_account_num()}')



    def submit(self):
        """
        Method to get the user inpout and compute the changes to the account
        """


        try:
            self.amount = float(self.input_amount.text())
            self.enter_account_num()

            if self.radio_deposit.isChecked():
                self.x = self.account.deposit(self.amount)
                self.choice = "Deposit"

            elif self.radio_withdraw.isChecked():
                self.x = self.account.withdraw(self.amount)
                self.choice = 'Withdraw'


            if self.x == False:
                self.label_output.setText(f'\tYou do not have enough in your\n\taccount to withdraw this amount.')
            elif self.x == True:
                self.label_output.setText(f' \t      ACCOUNT INFO\n\n'
                                          f'\t      Account Number: {self.account.get_account_num()}\n'
                                          f'\t      Total {self.choice}: ${self.amount:.2f}\n')





            dict[self.num] = self.account.get_balance()

            print(self.account.get_balance())
            self.input_amount.setText('')


        except ValueError:
            self.label_output.setText(f'    Only enter numbers in Account Balance\n    and Amount.')
            self.input_amount.setText('')
            self.input_num.setText('')




    def clear(self):
        """
        Method to clear the gui screen
        """
        self.label_output.setText('')
        self.label_num.setText('')
        self.label_amount.setText('')
        self.radio_deposit.setChecked(True)

    def check_balance(self):
        """
        Method to check the account balance and show it on screen
        """
        self.label_output.setText(f'\t    ACCOUNT NUMBER: {self.account.get_account_num()}\n'
                                  f'\t    BALANCE TOTAL: ${self.account.get_balance():.2f}')



