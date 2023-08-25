import abc


class Account(abc.ABC):
    """Account class."""
    def __init__(self, branch: int, account: str, balance: float = 0):
        """Constructor.

        Args:
            branch(int): branch number.
            account(str): account number.
            balance(float): balance value. Zero by default.
        """
        self.branch = branch
        self.account = account
        self.balance = balance

    @abc.abstractmethod
    def withdraw(self, value: int):
        """Withdraw abstract method.

        Args:
            value(int): withdrawal value.
        """
        ...

    def deposit(self, value: int):
        """Desposit method.

        Args:
            value(int): value to be deposited.
        """
        self.balance += value
        self.show_details(f'(Deposit) {value} dollars.')

    def show_details(self, message: str = ''):
        """Show account details method.

        Args:
            message(str): Show account value after deposit/withdraw. Empty by default.
        """
        print(f'Your actual balance is {self.balance:.2f} dollars.\n{message}')
        print('..'*50)

    def __repr__(self) -> str:
        """Repr class.

        Returns:
            string with class name and their attributes.
        """
        class_name = type(self).__name__
        attributes = f'({self.branch!r},{self.account!r},{self.balance!r})'
        return f'{class_name}{attributes}'


class SavingAccount(Account):
    """Saving Account class."""
    def withdraw(self, value: int) -> float:
        """Withdraw of saving account method.

        Args:
            value(int): withdrawal value.

        Returns:
            self.balance(float): balance account after withdraw.
        """
        withdrawal_value = self.balance - value

        if withdrawal_value >= 0:
            self.balance -= value
            self.show_details(f'(Withdraw) {value} dollars.')
            return self.balance
        print('It can not be possible withdraw the desired value.')
        self.show_details('(Withdraw) DENEID.')
        return self.balance


class CheckingAccount(Account):
    """Checking Account class."""
    def __init__(self, branch: int, account: str, balance: float = 0, protection: int = 0):
        """Constructor.

        Args:
            branch(int): branch number.
            account(str): account number.
            balance(float): balance value.
            protection(int): protection available. 0 by default.
        """
        super().__init__(branch, account, balance)
        self.protection = protection

    def withdraw(self, value: int) -> float:
        """Withdraw of checking account method.

        Args:
             value(int): withdraw value.

        Returns:
            self.balance(float): balance account after withdraw.
        """
        withdrawal_value = self.balance - value
        overdraft_credit = -self.protection

        if withdrawal_value >= overdraft_credit:
            self.balance -= value
            self.show_details(f'(Withdraw) {value} dollars.')
            return self.balance
        print('It can not be possible withdraw the desired value.')
        self.show_details('(Withdraw) DENEID.')
        return self.balance

    def __repr__(self):
        """Repr class.

        Returns:
            string with class name and their attributes.
        """
        class_name = type(self).__name__
        atributes = f'({self.branch!r},{self.account!r},{self.balance!r},{self.protection!r})'
        return f'{class_name}{atributes}'


if __name__ == '__main__':
    saving_account_1 = SavingAccount(branch=1, account='12345-0', balance=0)
    saving_account_1.withdraw(1)
    saving_account_1.deposit(1)
    saving_account_1.withdraw(1)
    print('##')
    checking_account_1 = CheckingAccount(branch=1, account='12346-0', balance=0, protection=100)
    checking_account_1.withdraw(1)
    checking_account_1.deposit(1)
    checking_account_1.withdraw(100)
    checking_account_1.withdraw(1)
