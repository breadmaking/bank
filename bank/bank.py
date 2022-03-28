from datetime import datetime
from .statement import Statement


class NoBalanceAvailable(Exception):
    def __init__(self, current_balance, withdraw_amount):
        self.error = (
            f"Your balance is {current_balance}."
            f"You do not have enough to withdraw {withdraw_amount}."
        )
        super().__init__(self.error)


class Account:
    def __init__(self, balance=0):
        self.balance = balance
        self.transactions = []

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        self.transactions.append(
            {
                "type": "deposit",
                "amount": deposit_amount,
                "date": datetime.now(),
                "current_balance": self.balance,
            }
        )

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance:
            raise NoBalanceAvailable(self.balance, withdraw_amount)
        else:
            self.balance -= withdraw_amount
            self.transactions.append(
                {
                    "type": "withdraw",
                    "amount": withdraw_amount,
                    "date": datetime.now(),
                    "current_balance": self.balance,
                }
            )

    def get_statement(self):
        statement = Statement(self.transactions)
        return statement.print_statement()
