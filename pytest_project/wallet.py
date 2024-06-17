
class InsufficientAmount(Exception):  #derived from exception class
    pass
class Wallet(object):
    def __init__(self,initial_amt=0):
        self.balance=initial_amt
    def spend_cash(self,amnt):
        if self.balance<amnt:
            raise InsufficientAmount("Not enough money  to spend {}".format(amnt))
        self.balance-=amnt
    def addCash(self,amnt):
        self.balance+=amnt


