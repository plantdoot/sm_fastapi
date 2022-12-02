import pytest
from app.calculations import add, subtract, multiply, divide, BankAccount, InsuffucientFunds

@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("num1, num2, expected", [
    (3, 2, 5),
    (5, 4, 9),
    (7, 1, 8)
])
def test_add(num1, num2, expected):
    assert add(num1, num2) == expected

def test_subtract():
    assert subtract(9, 4) == 5

def test_multiply():
    assert multiply(5, 4) == 20

def test_divide():
    assert divide(8, 4) == 2


def test_bank_set_inital_amount(bank_account):
    assert bank_account.balance == 50

def test_bank_default_amount(zero_bank_account):
    assert zero_bank_account.balance == 0

def test_withdraw(bank_account):
    bank_account.withdraw(20)
    assert bank_account.balance == 30

def test_deposit(bank_account):
    bank_account.deposit(20)
    assert bank_account.balance == 70

def test_collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance, 6) == 55


@pytest.mark.parametrize("deposited, withdrew, balance", [
    (200, 100, 100),
    (50, 40, 10),
    (3000, 500, 2500)
])
def test_bank_transaction(zero_bank_account, deposited, withdrew, balance):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == balance

def test_insufficient_funds(bank_account):
    with pytest.raises(InsuffucientFunds):
        bank_account.withdraw(200)
