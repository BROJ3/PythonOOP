#Bank that manages a dictionary of account objects

from bank_account import *

from bank import *

oBank = Bank()

my_acc_num = oBank.create_account('Toni',100,'toni')
print("Toni's acc number is: ", my_acc_num)

mary_acc_num = oBank.create_account('Mary',160,'mary')
print("Mary's acc number is: ", mary_acc_num)

while True:
    print()
    print("To get an acc balance, press b")
    print("To clse an acc, press c")
    print("To make a deposit, press d")
    print("To open an acc, press o")
    print("To quit press q")
    print("To show all acccounts, press s")
    print("To make a withdrawal, press w")
    print()

    action = input("What do you want to do?")
    action = action.lower()
    action = action[0]

    if action == 'b':
        oBank.balance()
    elif action == 'd':
        oBank.deposit()
    elif action == 'c':
        oBank.close_account()
    elif action == 'o':
        oBank.open_account()
    elif action == 's':
        oBank.show()
    elif action == 'w':
        oBank.withdraw()
    elif action == 'q':
        break
    else:
        print("Not a valid action, sorry")
