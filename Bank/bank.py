#Bank that manages a dictionary of account objects

from bank_account import *

class Bank():
    def __init__(self):
        self.accounts_dict = {}
        self.next_acc_num = 0

    def create_account(self,the_name,starting_amount,the_password):
        o_acc = Account(the_name,starting_amount,the_password)
        new_acc_num = self.next_acc_num
        self.accounts_dict[new_acc_num] = o_acc
        #incrementing
        self.next_acc_num +=1
        return new_acc_num
    
    def open_account(self):
        print("***OPEN ACCOUNT***")
        user_name = input("What is the name for this account?\n")
        user_starting_amount = int(input("What is the starting balance of this account? \n"))
        user_password = input("What is the password going to be?\n")
        user_acc_num = self.create_account(user_name,user_starting_amount, user_password)

        print("Your new account number is: ", user_acc_num)

    def close_account(self):
        print("***CLOSE ACCOUNT***")
        user_acc_num = int(input("What is your account number?"))
        user_password = input("Enter password please")
        o_acc = self.accounts_dict[user_acc_num]
        the_balance = o_acc.get_balance(user_password)
        if the_balance is not None:
            print("You had ", the_balance, " in your account, which is being returned to you")
        #remove user from dictionary
        del self.accounts_dict[user_acc_num]
        print("Your account is now closed")

    def balance(self):
        print("***GET BALANCE***")
        user_acc_num = int(input("What is your account number?"))
        user_password = input("Enter password please")
        o_acc = self.accounts_dict[user_acc_num]
        the_balance = o_acc.get_balance(user_password)
        if the_balance is not None:
            print("Your balance is: ", the_balance)

    def deposit(self):
        print("***DEPOSIT***")
        user_acc_number=input("Please enter your account number: ")
        user_acc_number = int(user_acc_number)
        user_deposit_amount = input("Enter amount to deposit: ")
        user_deposit_amount = int(user_deposit_amount)
        user_acc_password = input("Please enter the password\n")
        o_acc = self.accounts_dict[user_acc_number]
        the_balance = o_acc.deposit(user_deposit_amount,user_acc_password)
        if the_balance is not None:
            print("\nYour new balance is: ", the_balance)
    def show(self):
        print("***SHOW***")
        for user_acc_number in self.accounts_dict:
            o_acc = self.accounts_dict[user_acc_number]
            print("     Account Number: ", user_acc_number)
            o_acc.show()

    def withdraw(self):
        user_acc_number=input("Please enter your account number: ")
        user_acc_number = int(user_acc_number)
        user_withdraw_amount = input("Enter amount to withdraw: ")
        user_withdraw_amount = int(user_withdraw_amount)
        user_acc_password = input("Please enter the password\n")
        o_acc = self.accounts_dict[user_acc_number]
        the_balance = o_acc.withdraw(user_withdraw_amount,user_acc_password)
        if the_balance is not None:
            print("Withdrew: ", user_withdraw_amount)
            print("\nYour new balance is: ", the_balance)

    