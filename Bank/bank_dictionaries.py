#with dictionaries
#Non OOP version 5
#Any number of accounts

accounts_list=[]

def new_account(a_name,a_balance,a_password):
    global accounts_list
    new_account_dict = {
        'name':a_name,
        'balance':a_balance,
        'password':a_password
    }
    accounts_list.append(new_account_dict)

def show(account_number):
    global accounts_list
    print("Account: ",account_number)
    this_account_dict = accounts_list[account_number]
    print('     Name: ',this_account_dict['name'])
    print('     Balance: ',this_account_dict['balance'])
    print('     Password: ',this_account_dict['password'])
    print()

def get_balance(account_number,password):
    global accounts_list

    this_account_dict = accounts_list[account_number]
    if password != this_account_dict['password']:
        print("Incorrect password")
        return None
    return this_account_dict['balance']

def deposit(account_number,deposit_amount,password):
    global accounts_list
    this_account_dict = accounts_list[account_number]
    if password != this_account_dict['password']:
        print("incorrect password")
        return None
    if deposit_amount < 0:
        print("Cannot deposit negative account")
        return None
    this_account_dict['balance'] = this_account_dict['balance'] + deposit_amount
    return this_account_dict['balance']

def withdraw(account_number,withdraw_amount,password):
    global accounts_list
    this_account_dict = accounts_list[account_number]
    if password != this_account_dict['password']:
        print("Incorrect password")
        return None
    if withdraw_amount < 0:
        print("Cannot withdraw negative amount")
        return None
    if withdraw_amount > this_account_dict['balance']:
        print("Cannot withdraw more than you have")
        return None
    this_account_dict['balance'] = this_account_dict['balance']-withdraw_amount
    return this_account_dict['balance']

#sample accounts
print("Joe's account number", len(accounts_list))
new_account('Joe',100,'soup')
print("Beti's account number", len(accounts_list))
new_account('Beti',12345,'nuts')

while True:
    print()
    print('press b to get balance')
    print('press s to get details')
    print('press d to deposit')
    print('press w to witdraw')

    action = input("What do you want to do?")
    action = action.lower()
    action = action[0]
    print('\n')
    akcije = ['b','s','d','q','w','t']
    
    if action == 'b':
        print("get balance")
        user_account_number = input("please enter your account number\n")
        user_account_number = int(user_account_number)
        user_password = input('Please enter Password\n')
        the_balance = get_balance(user_account_number,user_password)
        if the_balance is not None:
            print("Your Balance is: ",the_balance)
    elif action == 's':
        account_number = int(input("Please select account"))
        show(account_number)
    elif action == 'd':
        user_account_number = int(input("Please enter account number\n"))
        user_deposit_amount = int(input("Enter deposit ampunt"))
        user_password = input("Please enter password\n")
        new_balance = deposit(user_account_number,user_deposit_amount,user_password)
        if new_balance is not None:
            print("Your new balance is: ", new_balance)
    elif action == 'w':
        user_account_number = int(input("Enter accout number:\n"))
        user_withdraw_amount = int(input("Enter amount to withdraw:\n"))
        user_password = input("Enter password")
        new_balance = withdraw(user_account_number,user_withdraw_amount,user_password)
        if new_balance is not None:
            print("Your new balance is: ", new_balance)
    elif action == 'n':
        print("New account:")
        user_name = input("What is your name")
        user_starting_mount = 0
        user_password = input("What would you like your password to be")

        user_account_number = len(accounts_list)
        new_account(user_name,user_starting_mount, user_password)
        print("Your account number will be: ", user_account_number)
    
    elif action == 'q':
        break 
    elif action not in akcije:
        print("Please Select a valid action")
        None