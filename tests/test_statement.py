from bank.statement import Statement
from datetime import datetime
import pytest


@pytest.fixture
def test_statement():
    statement = Statement(
            transactions=[
                {
                    "type": "deposit",
                    "amount": 1000,
                    "date": datetime(2023, 1, 10),
                    "current_balance": 1000,
                },
                {
                    "type": "withdraw",
                    "amount": 500,
                    "date": datetime(2023, 1, 14),
                    "current_balance": 2500,
                },
                {
                    "type": "deposit",
                    "amount": 2000,
                    "date": datetime(2023, 1, 13),
                    "current_balance": 3000,
                },

            ]
        )
    return statement


def test_statement_is_initialised_with_a_list_transactions(test_statement):
    assert type(test_statement.transactions) is list


def test_transactions_are_sorted_by_date(test_statement):
    sorted_dates = test_statement.sort_by_date()
    assert sorted_dates[0]['date'] > sorted_dates[1]['date'] > sorted_dates[2]['date']


def test_statement_is_generated_with_account_transactions(test_statement, capsys):
    test_statement.print_statement()
    out, err = capsys.readouterr()
    assert out == (
        "date || credit || debit || balance\n"
        "14/01/2023 || || 500.00 || 2500.00\n"
        "13/01/2023 || 2000.00 || || 3000.00\n"
        "10/01/2023 || 1000.00 || || 1000.00\n"
    )
    assert err == ""
