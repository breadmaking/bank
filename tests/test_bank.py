from datetime import datetime
from unittest.mock import patch
import pytest
from freezegun import freeze_time
from bank.bank import Account, NoBalanceAvailable


@pytest.fixture
def test_account():
    account = Account()
    return account


def test_bank_account_has_balance(test_account):
    assert test_account.balance == 0


def test_bank_account_balance_increases_on_deposit(test_account):
    test_account.deposit(1000)
    assert test_account.balance == 1000


def test_bank_account_balance_decreases_on_withdraw(test_account):
    test_account.deposit(1000)
    test_account.withdraw(500)
    assert test_account.balance == 500


def test_bank_account_stores_an_action(test_account):
    assert test_account.transactions == []


@freeze_time("2022-03-27")
def test_bank_account_stores_a_deposit(test_account):
    test_account.deposit(1000)
    assert test_account.transactions == [
        {
            "type": "deposit",
            "amount": 1000,
            "date": datetime(2022, 3, 27),
            "current_balance": 1000,
        }
    ]


@freeze_time("2022-03-27")
def test_bank_account_stores_multiple_deposits(test_account):
    test_account.deposit(1000)
    test_account.deposit(500)
    assert test_account.transactions == [
        {
            "type": "deposit",
            "amount": 1000,
            "date": datetime(2022, 3, 27),
            "current_balance": 1000,
        },
        {
            "type": "deposit",
            "amount": 500,
            "date": datetime(2022, 3, 27),
            "current_balance": 1500,
        },
    ]


@freeze_time("2022-03-27")
def test_bank_account_stores_a_withdraw(test_account):
    test_account.deposit(1000)
    test_account.withdraw(1000)
    assert test_account.transactions == [
        {
            "type": "deposit",
            "amount": 1000,
            "date": datetime(2022, 3, 27),
            "current_balance": 1000,
        },
        {
            "type": "withdraw",
            "amount": 1000,
            "date": datetime(2022, 3, 27),
            "current_balance": 0,
        },
    ]


@freeze_time("2022-03-27")
def test_bank_account_stores_multiple_withdraws(test_account):
    test_account.deposit(1000)
    test_account.withdraw(500)
    test_account.withdraw(250)
    assert test_account.transactions == [
        {
            "type": "deposit",
            "amount": 1000,
            "date": datetime(2022, 3, 27),
            "current_balance": 1000,
        },
        {
            "type": "withdraw",
            "amount": 500,
            "date": datetime(2022, 3, 27),
            "current_balance": 500,
        },
        {
            "type": "withdraw",
            "amount": 250,
            "date": datetime(2022, 3, 27),
            "current_balance": 250,
        },
    ]


def test_withdraw_cannot_exceed_balance_total(test_account):
    with pytest.raises(NoBalanceAvailable) as e:
        test_account.withdraw(500)
        assert str(e.value) == (
            "Your balance is 0." "You do not have enough to withdraw 500."
        )


@patch("bank.bank.datetime")
def test_account_can_get_statement(datetime_mock, test_account, capsys):
    datetime_mock.now.return_value = datetime(2023, 1, 10)
    test_account.deposit(1000)
    datetime_mock.now.return_value = datetime(2023, 1, 13)
    test_account.deposit(2000)
    datetime_mock.now.return_value = datetime(2023, 1, 14)
    test_account.withdraw(500)
    test_account.get_statement()
    out, err = capsys.readouterr()
    assert out == (
        "date || credit || debit || balance\n"
        "14/01/2023 || || 500.00 || 2500.00\n"
        "13/01/2023 || 2000.00 || || 3000.00\n"
        "10/01/2023 || 1000.00 || || 1000.00\n"
    )
    assert err == ""
