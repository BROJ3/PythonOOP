from bank_account import *

accounts_dict = {}
next_acc_number = 0
 
o_acc = Account('Joe',100,'joes')
joes_acc_num = next_acc_number
accounts_dict[joes_acc_num] = o_acc
print("Joe's account number is: ", joes_acc_num)

next_acc_number = next_acc_number+1

o_acc = Account('Mary',100,'marys')
marys_acc_num = next_acc_number  
accounts_dict[marys_acc_num] = o_acc
print("Marys acc number is: ", marys_acc_num)

next_acc_number = next_acc_number+1

accounts_dict[joes_acc_num].show()
accounts_dict[marys_acc_num].show()

while True:
    print()
    print("Press b to get the balance")
    print("Press d to make a deposit")
    print("Press o to open a new account")
    print("Press w to make a withdrawal")
    print("Press s to show all accounts")
    print("Press q to quit")
    print()

    action = input("What would you like to do?")
    action = action.lower()
    action = action[0]
    if action == "b":        
        print("***Get Balance***")
        user_acc_number=input("Please enter your account number: ")
        user_acc_number = int(user_acc_number)
        user_acc_password = input("Please enter the password\n")
        o_acc = accounts_dict[user_acc_number]
        the_balance = o_acc.get_balance(user_acc_password)
        if the_balance is not None:
            print("\nYour balance is: ", the_balance)

    elif action == 'd':
        print("***DEPOSIT***")
        user_acc_number=input("Please enter your account number: ")
        user_acc_number = int(user_acc_number)
        user_deposit_amount = input("Enter amount to deposit: ")
        user_deposit_amount = int(user_deposit_amount)
        user_acc_password = input("Please enter the password\n")
        o_acc = accounts_dict[user_acc_number]
        the_balance = o_acc.deposit(user_deposit_amount,user_acc_password)
        if the_balance is not None:
            print("\nYour new balance is: ", the_balance)

    elif action == 'o':
        print("*** Open Account ***")
        user_name = input("What is the name for this account?\n")
        user_starting_amount = int(input("What is the starting balance of this account? \n"))
        user_password = input("What is the password going to be?\n")
        o_acc = Account(user_name, user_starting_amount, user_password)
        accounts_dict[next_acc_number] = o_acc
        print("Your new accout number is: ", next_acc_number)
        next_acc_number +=1
        print()
    elif action == 'w':
        print("*** WITHDRAW ***")
        user_acc_number=input("Please enter your account number: ")
        user_acc_number = int(user_acc_number)
        user_withdraw_amount = input("Enter amount to withdraw: ")
        user_withdraw_amount = int(user_withdraw_amount)
        user_acc_password = input("Please enter the password\n")
        o_acc = accounts_dict[user_acc_number]
        the_balance = o_acc.withdraw(user_withdraw_amount,user_acc_password)
        if the_balance is not None:
            print("\nYour new balance is: ", the_balance)
    elif action == 's':
        print("Show")
        for user_acc_num in accounts_dict:
            o_acc = accounts_dict[user_acc_num]
            print("     Account number: ", user_acc_num)
            o_acc.show()

    elif action == 'q':
        break

    else:
        print("sorry, not a vald action")