from Bank import *
from User import *
from Admin import *
def main():
    # create a bank
    bank = Bank('Bank_Alexa',3000)
    #create an admin 
    admin_jhon = Admin('Jhon Doe','jhon@doe.com','#####')
    admin_jhon.create_account(bank)
    # create some user 
    user_abul = User('Abul','abul@mia.com','####')
    user_babul = User('Babul','babul@mia.com','####')
    bank.create_account(user_abul)
    bank.create_account(user_babul)
    #deposit withdraw loan transfer
    bank.deposit(user_abul,50000)
    bank.deposit(user_babul,50000)
    bank.withdraw(user_abul,1000)
    user_abul.transfer_money(user_babul,30000)
    bank.get_loan(user_abul,38000)
    bank.get_loan(user_abul,14000)
    bank.deposit(user_abul,38000)
    # loan feature
    admin_jhon.loan_feature('off')
    bank.get_loan(user_babul,30000)
    admin_jhon.loan_feature('on')
    bank.get_loan(user_babul,30000)
    #history of abul
    #user_abul.show_transition()
    # babul check his balance 
    print('babul available balance:',user_babul.check_balance())
    bank.withdraw(user_abul,59000)
    #test admin 
    print('Form Admin')
    print('balance: ',admin_jhon.total_available_balance())
    print('loan balance',admin_jhon.total_loan_amount())
    bank.balance(user_abul)
    print(bank)



    pass 

if __name__ == '__main__':
    main()