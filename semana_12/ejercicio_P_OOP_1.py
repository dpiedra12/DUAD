class BankAccount:

    def __init__(self, balance):
        self.balance = balance
        

    def deposit_money(self, d_money ):
        self.d_money= d_money
        self.balance = self.balance + self.d_money
        print(self.balance )


    def withdraw_money(self, w_money): 
        self.w_money = w_money
        self.balance = self.balance - self.w_money
        print (self.balance )       


class SavingsAccount(BankAccount):

    def __init__(self, min_balance, balance):
        self.min_balance = min_balance
        super().__init__(balance)

    def withdraw_money(self, w_money):
        
        if self.balance - w_money >= self.min_balance:
            super().withdraw_money(w_money)
            return 
        
        else:
            raise ValueError ("Error: The balance is below the minimum balance.")
              

account1 = SavingsAccount(0,100)
account1.withdraw_money(90)

account2 = BankAccount(0)
account2.deposit_money(100)
account2.withdraw_money(12)
