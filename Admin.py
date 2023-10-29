from Bank import * 
from Persons import Person

class Admin(Person):
    def __init__(self, name, email, password) -> None:
        super().__init__(name, email, password)
        self.bank = None 
    def create_account(self,bank):
        self.bank = bank 
        bank.admin = self
    def total_available_balance(self):
        money = self.bank.balance(self)
        return money
    def total_loan_amount(self):
        print(self.bank.loan)
        return self.bank.loan 
    def loan_feature(self, status):
        if(status=='off'):
            self.bank.off_by_admin = True
        else :
            self.bank.off_by_admin = False