from dataclasses import dataclass


@dataclass
class Statement:
    def __init__(self, transactions: list[dict]):
        self.transactions = transactions

    def sort_by_date(self):
        self.transactions.sort(key=lambda item: item["date"], reverse=True)
        return self.transactions

    def print_statement(self):
        str_list = ["date || credit || debit || balance"]
        sorted_transactions = self.sort_by_date()
        for transaction in sorted_transactions:
            if transaction["type"] == "deposit":
                str = (
                    f"{transaction['date'].strftime('%d/%m/%Y')} || "
                    f"{'{0:.2f}'.format(transaction['amount'])} || || "
                    f"{'{0:.2f}'.format(transaction['current_balance'])}"
                )
                str_list.append(str)
            else:
                str = (
                    f"{transaction['date'].strftime('%d/%m/%Y')} || || "
                    f"{'{0:.2f}'.format(transaction['amount'])} || "
                    f"{'{0:.2f}'.format(transaction['current_balance'])}"
                )
                str_list.append(str)

        return print("\n".join(str_list))
