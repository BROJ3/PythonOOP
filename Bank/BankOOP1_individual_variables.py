#test program using accounts
#version1

from bank_account import *

Joe_account=Account('Joe',100,'joespassword')
print('Created an account for ' + Joe_account.name)

Marys_account=Account('Mary',11500,'marysspassword')
print('Created an account for ' + Marys_account.name)


#call some methods from 2 different accounts
print("Calling methods of the two accounts...")
'''
Joe_account.deposit(50,'joespassword')
Marys_account.withdraw(1500,'marysspassword')
Marys_account.deposit(100,'marysspassword')

Joe_account.show()
Marys_account.show()
'''


user_name = input("What is the name of the new user account?")
user_balance=input("What is the starting balance for this account?")
user_balance=int(user_balance)
user_password=input("What would you like the password to be?")
o_new_account = Account(user_name,user_balance,user_password)
o_new_account.show()

o_new_account.deposit(100,user_password)
user_balance=o_new_account.get_balance(user_password)
print()
print("After depositing 100 the user balance is now ", o_new_account.balance)
print(user_balance)

o_new_account.show()