#Non OOP version 4

account_names_list=[]
account_balances_list=[]
account_passwords_list=[]

def new_account(name, balance, password):
    global account_names_list, account_balances_list, account_passwords_list
    account_names_list.append(name)
    account_balances_list.append(balance)
    account_passwords_list.append(password)

def show(account_number):
    global account_names_list,account_balances_list,account_passwords_list
    print('     Account: ', account_number)
    print('     Balance: ', account_balances_list[account_number])
    print('     Password: ', account_passwords_list[account_number])
    print()

def getBalance(account_number, password):
        global account_names_list,account_balances_list,account_passwords_list
        if password !=account_passwords_list[int(account_number)]:
             print('Incorrect Password')
             return None
        return account_balances_list[int(account_number)]

def deposit(account_number, amount_to_deposit ,password):
    global account_names_list,account_balances_list,account_passwords_list

    if amount_to_deposit < 0:
         print("You cannot deposit a negative amount")
         return None
    if password != account_passwords_list[int(account_number)]:
         print("Incorrect Password")
         return None
    account_balances_list[int(account_number)] = account_balances_list[int(account_number)] + amount_to_deposit
    return account_balances_list[int(account_number)]

def withdraw(account_number,amount_to_withdraw,password):
    global account_names_list,account_balances_list,account_passwords_list

    if amount_to_withdraw > account_balances_list[int(account_number)]:
         print("How do you expect to withdraw more than you have")
         return None
    if amount_to_withdraw < 0:
         print("You cannot withdraw less than 0!")
         return None
    if password != account_passwords_list[int(account_number)]:
        print("Incorrect password")
        return None
    account_balances_list[int(account_number)] = account_balances_list[int(account_number)] - amount_to_withdraw
    return account_balances_list[int(account_number)]    

def transfer(account_number, receiver_account, amount_to_transfer, password):
    global account_names_list,account_balances_list,account_passwords_list

    if amount_to_transfer > account_balances_list[int(account_number)]:
        print("You cannot transfer more than you have in your account")
        return None
    if amount_to_transfer < 0:
         print("You cannot transfer a negative number!")
         return None
    if password !=account_passwords_list[int(account_number)]:
         print("Incorrect password!")
         return None
    else:
        print("Logic Successful!")
        print("Processing...")
        account_balances_list[int(account_number)] = account_balances_list[int(account_number)] - amount_to_transfer
        account_balances_list[int(receiver_account)] =account_balances_list[int(receiver_account)] + amount_to_transfer
        return account_balances_list[int(account_number)]


print("Joe's account number: ", len(account_names_list))
new_account("Joe",100,"soup")
print("Mary's account number: ", len(account_names_list))
new_account("Mary",500,"nuts")
print("Johnny's account number: ", len(account_names_list))
new_account("Johnny",300,"koka")
print("Jozo's account number: ", len(account_names_list))
new_account("Jozo",200,"kola")



while True:
    akcije = ['b','s','d','q','w','t']

    print("=================================")
    print(' press b to get balance')
    print(" press s to show details")
    print(" press d to deposit")
    print(" press w to withdraw")
    print(" Soon adding feature to press t to transfer")
    print("=================================")


    action = input("What do you want to do?")
    action = action.lower()
    action=action[0]
    if action == 'b':
        account_number = input("Please enter your account number")
        user_password = input("Password please")
        the_balance = getBalance(account_number,user_password)
        if the_balance is not None:
            print(the_balance)
    elif action == 's':
        account_number = input("Show details for which account?")
        account_number = int(account_number)
        show(account_number)
    elif action == 'd':
        print("Deposit\n")
        account_number = input("Please choose an account: ")
        amount_to_deposit = int(input("Enter Deposit Amount: "))
        user_password = input("Enter Password Please: ")  
        new_balance = deposit(account_number,amount_to_deposit,user_password)
        if new_balance is not None:
             print("Your New Balance is: ", new_balance)
    elif action == 'w':
         print("Withdraw\n")
         account_number = input("Please Choose an account")
         amount_to_withdraw = int(input("Enter amount to Withdraw: "))
         user_password = input("Enter Password: ")
         new_balance = withdraw(account_number, amount_to_withdraw, user_password)
         if new_balance is not None:
              print("Your New Balance is: ", new_balance)

    elif action == 't':
         print("Transfer\n")
         account_number = input("Please Choose an account")
         receiver_account = input("Please choose a receiveing account:")
         amount_to_transfer = int(input("Enter amount to Transfer"))
         user_password = input("Enter Password")
         new_balance = transfer(account_number,receiver_account,amount_to_transfer,user_password)
         if new_balance is not None:
              print("Your new balance: ", new_balance)

    elif action == 'q':
        break 
    elif action not in akcije:
        print("Please Select a valid action")
        None