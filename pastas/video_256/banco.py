from pessoas import Client
from contas import Account, SavingAccount, CheckingAccount


class Bank:
    """Bank class."""
    def __init__(self, branchs: list[int] = None, clients: list[Client] = None, accounts: list[Account] = None):
        """Constructor.

        Args:
            branchs(list[int]): lists of branchs. None by default.
            clients(list[Client]): lists of clients. None by default.
            accounts(list[Account]): lists of accounts. None by default.
        """
        self.branchs = branchs or []
        self.clients = clients or []
        self.accounts = accounts or []

    def _check_branch(self, account: Account) -> bool:
        """Checks if branch belongs to the list of branchs.

        Args:
            account(Account): account number.

        Returns:
            True if belongs.False if not belongs.
        """
        if account.branch in self.branchs:
            return True
        return False

    def _check_client(self, client: Client):
        """Checks if client belongs to the list of clients.

        Args:
            client(Client): client data.

        Returns:
            True if belongs.False if not belongs.
        """
        if client in self.clients:
            return True
        return False

    def _check_account(self, account: Account):
        """Checks if account belongs to the list of accounts.

        Args:
            account(Account): account number.

        Returns:
            True if belongs.False if not belongs.
        """
        if account in self.accounts:
            return True
        return False

    @staticmethod
    def _check_account_owner(client: Client, account: Account):
        """Checks if account belongs to client.

        Args:
            client(Client): client data.
            account(Account): account number.

        Returns:
            True if belongs. False if's does not.
        """
        if account is client.account:
            return True
        return False

    def authenticate(self, client: Client, account: Account):
        """Checks if all methods to check data of client and account are True.

        Args:
            client(Client): client data.
            account(Account): account number.

        Returns:
            True if all methods are True. False if at least one is False.
            """
        return self._check_branch(account) and self._check_client(client) and self._check_account(account) and \
            self._check_account_owner(client, account)

    def __repr__(self) -> str:
        """Repr method.

        Returns:
            string with class name and their attributes.
        """
        class_name = type(self).__name__
        attributes = f'({self.branchs!r},{self.clients},{self.accounts})'
        return f'{class_name}{attributes}'


if __name__ == '__main__':
    client_1 = Client('Maria', 24)
    checking_account_1 = CheckingAccount(branch=111, account='22222-2', balance=0, protection=0)
    client_1.account = checking_account_1
    client_2 = Client('Luiz', 30)
    saving_acccount_1 = SavingAccount(branch=112, account='22322-5', balance=100)
    client_2.account = saving_acccount_1
    bank = Bank()
    bank.clients.extend([client_1, client_2])
    bank.accounts.extend([checking_account_1, saving_acccount_1])
    bank.branchs.extend([111, 112])

    if bank.authenticate(client_1, checking_account_1):
        checking_account_1.show_details()
        checking_account_1.deposit(150)
        checking_account_1.withdraw(20)
        checking_account_1.show_details()
        print(client_1.account)
