from datetime import date
class History:
    def __init__(self,name,status,amount,balance) -> None:
        self.name = name
        self.status = status 
        self.amount = amount
        self.balance = balance
    def __repr__(self) -> str:
        txt = f'{self.name} At {date.today()} {self.status} TK {self.amount} after balance {self.balance}'
        return txt