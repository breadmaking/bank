from datetime import datetime


class NoBalanceAvailable(Exception):
    def __init__(self, curent_balance, withdraw_amount):
        self.error = (
            f"Your balance is {curent_balance}."
            f"You do not have enough to withdraw {withdraw_amount}."
        )
        super().__init__(self.error)


class Account:
    def __init__(self, balance=0):
        self.balance = balance
        self.actions = []

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        self.actions.append(
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
            self.actions.append(
                {
                    "type": "withdraw",
                    "amount": withdraw_amount,
                    "date": datetime.now(),
                    "current_balance": self.balance,
                }
            )

    def print_statement(self):
        str_list = ["date || credit || debit || balance"]
        self.actions.sort(key=lambda item: item["date"], reverse=True)
        for action in self.actions:
            if action["type"] == "deposit":
                str = (
                    f"{action['date'].strftime('%d/%m/%Y')} || "
                    f"{'{0:.2f}'.format(action['amount'])} || || "
                    f"{'{0:.2f}'.format(action['current_balance'])}"
                )
                str_list.append(str)
            else:
                str = (
                    f"{action['date'].strftime('%d/%m/%Y')} || || "
                    f"{'{0:.2f}'.format(action['amount'])} || "
                    f"{'{0:.2f}'.format(action['current_balance'])}"
                )
                str_list.append(str)

        return print("\n".join(str_list))
