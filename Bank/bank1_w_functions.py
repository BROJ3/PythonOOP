# Non OOP
# Bank 2
# Single account

account_name = ''
account_balance = 0
account_password = ''

def new_acc(name,balance,password):
    global account_name, account_balance, account_password
    account_name = name
    account_balance = balance
    account_password = password

def show():
    global account_name, account_balance, account_password
    print('     Name', account_name)
    print('     Balance', account_balance)
    print('     Password', account_password)
    print()


def get_balance(password):
    global account_name,account_balance, account_password
    if password != account_password:
        print('Incorrect password')
        return None
    return account_balance


def deposit(amount_to_deposit,password):
    global account_name,account_balance, account_password
    if amount_to_deposit < 0:
        print("You cannot deposit a negative amount!")
        return None
    if password != account_password:
        print('Incorrect password')
        return None
    
    account_balance = account_balance + amount_to_deposit
    return account_balance

def withdraw(amount_to_withdraw, password):
    global account_name,account_balance, account_password
    if amount_to_withdraw < 0:
        print('Cannot withdraw negative amount!')
        return None
    if password != account_password:
        print("Incorrect password!")
        return None
    if amount_to_withdraw > account_balance:
        print("You cannot withdraw more than you have in your account")
        return None
    account_balance = account_balance - user_withdraw_amount
    return account_balance

new_acc('Djole',1000,'trump')


while True:
    print('==============')
    print('press b to get balance')
    print('press d to make a deposit')
    print('press w to make a withdrawal')
    print('press s to show the account')
    print('press q to quit')
    print('==============')
 
    action = input('What do you want to do')
    action = action.lower() #making sure its lowercase
    action = action[0] #just use first letter
    print()
    if action == 'b':
        print('Get Balance:')
        user_password = input("Please enter the password")
        balance = get_balance(user_password)
        if balance is not None:
            print('Your balance is: ', balance)
    elif action == 'd':
        print("Deposit: ")
        user_deposit_amount = input("enter amount to deposit: ")
        user_deposit_amount = int(user_deposit_amount)
        user_password = input('Plese enter user password')

        new_balance = deposit(user_deposit_amount, user_password)
        if new_balance is not None:
            print('Your new balance is: ', new_balance)
    elif action == 's':
        show()
    elif action == 'w':
        print("Withdraw:")
        user_withdraw_amount = input("Please enter the amount to withdraw")
        user_withdraw_amount = int(user_withdraw_amount)
        user_password = input("Enter Password: ")
        new_balance = withdraw(user_withdraw_amount, user_password)
        if new_balance is not None: \
            print("Your new balace is ",balance)
    elif action == 'q':
        break
