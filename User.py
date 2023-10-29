from History import History
from Persons import Person
class User(Person):
    def __init__(self,name,email,password,amount=0) -> None:
        super().__init__(name,email,password)
        self.balance = amount
        self.loan_balance = 0
        self.id = None
        self.history = []
    def check_balance(self):
        return self.balance
    def transfer_money(self,other_user,amount):
        if(amount<=self.balance):
            self.balance -= amount
            other_user.balance += amount
            details = History(self.name,'TRANSFER',amount,self.balance)
            print(details)

    def show_transition(self):
        print(f'History of {self.name}')
        for ele in self.history:
            print(ele)
        print('\n')
   