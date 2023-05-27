from BankOOP6_using_exceptions_bank import *

o_bank = Bank('9 to 5','123 Main Street, Anytown, USA','(650) 555-1212')

while True:
    print()
    print("To get an account balance, press b")
    print("To close an account, press c")
    print("To make a deposit, press d")
    print("To get bank information, press i")
    print("To open a new account, press o")
    print("To quit, press q")
    print("To show all accounts, press s")
    print("To make a withdrawal, press w")
    print()

    action=input("What would you like to do?\n")
    action=action.lower()
    action=action[0]
    
    try:  
        if action == 'b':
            o_bank.balance()
        elif action == 'd':
            o_bank.deposit()
        elif action == 'w':
            o_bank.withdraw()
        elif action =='o':
            o_bank.open_acc()
        elif action == 'c':
            o_bank.close_acc()
        elif action == 's':
            o_bank.show()
        elif action == 'i':
            o_bank.get_info()
        elif action == 'q':
            print("This was a triumph...")
            break

        

    except abort_transaction as error:
        print(error)