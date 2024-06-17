import pytest
from wallet import Wallet,InsufficientAmount

# data to run test case fixture is used
# gives empty wallet with balce 0 and call constructor wallet
@pytest.fixture
def empty_wallet():
    return Wallet()
# gives wallet with balce 20 and call constructor wallet
@pytest.fixture
def wallet():
    return Wallet(20)

# check inittal balnce should be 0 for empty wallet
def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance==0

# checking iitnal ammount of wallet is 20
def test_setting_initial_amount(wallet):
    assert wallet.balance==20

# check  after adding cash gives correct amount 100 for 20 inital amnt 80+20=100
def test_valid_add_cash(wallet):
    wallet.addCash(80)
    assert wallet.balance==100

# check spend cash is corect
def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance==10

def test_wallet_spend_cash_raises_exception_of_insufficient_balance(empty_wallet):
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)