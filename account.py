
class Account:
    """
    A class representing details for an account object
    """
    def __init__(self, number: int) -> None:
        """
        Constructor to set default values for an account object
        :param number: Account number
        """

        self.__account_num = int(number)
        self.__account_balance: float = 0



    def deposit(self, amount: float) -> bool:
        """
        Method to increase the account balance
        :param amount: The amount to increase
        :return: True if successful, False if unsuccessful
        """
        try:
            if amount > 0:
                self.__account_balance += amount
                return True
            else:
                return False
        except:
            raise ValueError


    def withdraw(self, amount: float) -> bool:
        """
        Method to decrease the account balance
        :param amount: The amount to decrease
        :return: True if successful, False if unsuccessful
        """
        try:
            if 0 < amount <= self.__account_balance:
                self.__account_balance -= amount
                return True
            else:
                return False



        except:
            raise ValueError

    def get_balance(self) -> float:
        """
        Method to access an accounts balance
        :return: Account balance
        """
        return self.__account_balance

    def get_account_num(self) -> int:
        """
        Method to access an accounts number
        :return: Account number
        """
        return self.__account_num


if __name__ == '__main__':
    pass