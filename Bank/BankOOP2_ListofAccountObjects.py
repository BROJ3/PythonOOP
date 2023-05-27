#Test program using accounts
#Version 2

from bank_account import *

accounts_list = []
o_account=Account('Joe',100,'joespass')
accounts_list.append(o_account)
print("Joe's account number is 0")

o_account=Account('Mary',100,'maryspass')
accounts_list.append(o_account)
print("Joe's account number is 1")

accounts_list[0].show()
accounts_list[1].show()
print()

print("Calling methods of 2 accounts....")

accounts_list[0].deposit(500,'joespass')
accounts_list[1].withdraw(50,'maryspass')
accounts_list[1].deposit(200,'maryspass')
accounts_list[1].withdraw(10,'maryspass')
print('initializing...')
accounts_list[0].show()
accounts_list[1].show()

user_name = input("What is the name of the new user account?")
user_balance=input("What is the starting balance for this account?")
user_balance=int(user_balance)
user_password=input("What would you like the password to be?")
o_new_account = Account(user_name,user_balance,user_password)
accounts_list.append(o_new_account)

print("Created new account, acc number is ", len(accounts_list)-1)
accounts_list[2].show()
accounts_list[2].deposit(1000000,'tonci')
user_balance = accounts_list[2].get_balance(user_password)

print("After the deposit, the account no.2 now has:", accounts_list[2].get_balance(user_password), ' dollrss in his account.' )
accounts_list[2].show()