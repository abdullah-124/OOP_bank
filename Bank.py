from History import History
class Bank:
    def __init__(self,name,amount=0) -> None:
        self.name = name
        self.__balance = amount
        self.users = []
        self.admin = None
        self.loan = 0
        self.loan_status = True
        self.off_by_admin = False

    def create_account(self,user):
        user.id = f'{self.name}-{user.name}-{len(self.users)+1000001}'
        self.users.append(user)

    def deposit(self,user,amount):
        if(amount>=100):
            user.balance += amount 
            details = History(user.name,'DEPOSIT',amount,user.balance)
            user.history.append(details)
            self.__balance += amount
            print(details)

    def withdraw(self,user,amount):
        if(user.balance>=amount):
            if(self.__balance>=amount):
                user.balance -= amount
                self.__balance -= amount
                details = History(user.name,'WITHDRAW',amount,user.balance)
                user.history.append(details)
                print(details)
                return amount 
            else :
                print('the bank is bankrupt....')
                return -1
        else :
            print('Insufficient Ballance...')
            return 0
        
    def get_loan(self,user,amount):
        if(self.off_by_admin==True):
            print('Loan Feature off....')
        elif(self.loan+amount >= self.__balance):
            self.loan_status = False
        elif(self.loan+amount<self.__balance) :
            self.loan_status = True
        if self.loan_status==False:
            print('Loan Feature Off')
        elif(amount <= 2*user.balance):
            self.__balance -= amount
            self.loan += amount
            user.loan_balance += amount
            user.balance += amount 
            details = History(user.name,'LOAN',amount,user.balance)
            user.history.append(details)
            print(details)
        else :
            print('your loan limit Over')
       
    def balance(self,user):
        if(user == self.admin):
            return self.__balance
        else :
            print('bad request 502')
            return -1
            




    def __repr__(self) -> str:
        print('##########################')
        print(self.name)
        print(f'Balance: {self.__balance} loan : {self.loan} loan_status: {self.loan_status}')
        print('------------USER--------------')
        print('Name\t\t Balance')
        for user in self.users:
            print(user.name,'\t',user.balance)
        print('\n')
        print('------Admin-------')
        print('Name',self.admin.name)
        print('Email',self.admin.email)
        return f'{self.name} copyright 2023\n----------------------'
    