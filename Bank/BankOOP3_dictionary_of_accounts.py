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

print("Calling methods...")

accounts_dict[joes_acc_num].deposit(150,'joes')
accounts_dict[marys_acc_num].withdraw(50,'marys') 
accounts_dict[marys_acc_num].deposit(450,'marys')


accounts_dict[joes_acc_num].show()
accounts_dict[marys_acc_num].show()

user_name = input("What is the name of the new user account?")
user_balance=input("What is the starting balance for this account?")
user_balance=int(user_balance)
user_password=input("What would you like the password to be?")
o_acc=Account(user_name,user_balance,user_password)
new_acc_num = next_acc_number 
accounts_dict[new_acc_num] = o_acc
print("Acc number for the new account is ", new_acc_num)
next_acc_number = next_acc_number+1

accounts_dict[new_acc_num].show()

accounts_dict[new_acc_num].deposit(150,user_password)
user_balance=accounts_dict[new_acc_num].get_balance(user_password)
print("After depositing 150, the user's balance is: ", user_balance)

accounts_dict[new_acc_num].show()