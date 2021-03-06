# Bank tech test

## Set Up / Installation

Install [Python](https://wiki.python.org/moin/BeginnersGuide/Download)

```
pip install --user pipenv
```
```
run pipenv shell
```

### To run tests:
```
pytest
```
### To run tests with coverage:
```
pytest --cov
```
### To run flake8 liner:
```
flake8
```

## How to use the program
Open terminal
```
python
```
Import Class
```
from bank.bank import Account
```
Create Account
```
account = Account()
```
Make a deposit
```
account.deposit(1000)
```
Make a withdrawl
```
account.withdraw(500)
```
Print account statement
```
account.print_statement()
```

## Specification

### Requirements

* You should be able to interact with your code via a REPL like IRB or Node.  (You don't need to implement a command line interface that takes input from STDIN.)
* Deposits, withdrawal.
* Account statement (date, amount, balance) printing.
* Data can be kept in memory (it doesn't need to be stored to a database or anything).

### Acceptance criteria

**Given** a client makes a deposit of 1000 on 10-01-2023  
**And** a deposit of 2000 on 13-01-2023  
**And** a withdrawal of 500 on 14-01-2023  
**When** she prints her bank statement  
**Then** she would see

```
date || credit || debit || balance
14/01/2023 || || 500.00 || 2500.00
13/01/2023 || 2000.00 || || 3000.00
10/01/2023 || 1000.00 || || 1000.00
```

```
----------------------- Captured stdout call -----------------------
date || credit || debit || balance
14/01/2023 || || 500.00 || 2500.00
13/01/2023 || 2000.00 || || 3000.00
10/01/2023 || 1000.00 || || 1000.00
```

<!-- END GENERATED SECTION DO NOT EDIT -->
