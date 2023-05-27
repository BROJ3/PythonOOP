# Non-OOP
# Bank 3
# Two acounts

account_0_name = 'toni'
account_0_balance = 1000
account_0_password = 'toni'
account_1_name = 'jedan'
account_1_balance = 1500
account_1_password = 'jedan'
n_accounts = 0

def new_acc(account_number, name, balance, password):
    global account_0_name, account_0_balance, account_0_password
    global account_1_name, account_1_balance, account_1_password
 
    if account_number == 0:
        account_0_name = name
        account_0_balance = balance
        account_0_password = password
    if account_number == 1:
        account_1_name = name
        account_1_balance = balance
        account_1_password = password

  
def show():
    global account_0_name, account_0_balance, account_0_password
    global account_1_name, account_1_balance, account_1_password
    
    if account_number == 0:
        print('Account 0')
        print('     Name: ', account_0_name)
        print('     Balance: ', account_0_balance)
        print('     Password: ', account_0_password)
    
    if account_number == 1:
        print('Account 1')
        print('     Name: ', account_1_name)
        print('     Balance: ', account_1_balance)
        print('     Password: ', account_1_password)
        

    
def get_balance(account_number, password):
    global account_0_name, account_0_balance, account_0_password
    global account_1_name, account_1_balance, account_1_password
    
    if account_number == 0:
        if password != account_0_password:
            print('Incorrect password!')
            return None
        return account_0_balance

    if account_number == 1:
        if password != account_1_password:
            print('Incorrect password!')
            return None
        return account_1_balance
        
while True:
    print('==============')
    print('press b to get balance')
 
    action = input('What do you want to do')
    action = action.lower() #making sure its lowercase
    action = action[0] #just use first letter
    print()
    if action == 'b':
        print('Get Balance:')

        account_number = input("Please enter acc number")
        
        password = input("Please enter the password")
        balance = get_balance(account_number, password)
        if balance is not None:
            print('Your balance is: ', balance)



