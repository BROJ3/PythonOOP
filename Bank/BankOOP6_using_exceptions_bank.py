#bank that manages account objects

from BankOOP6_exceptions_account import *

class Bank():

    def __init__(self, hours,address,phone):
        self.accounts_dict = {}
        self.next_acc_num = 0
        self.hours = hours
        self.address = address
        self.phone = phone

    def ask_for_valid_acc_num(self):
        acc_num = input("What is your account number?\n")
        try:
            acc_num = int(acc_num)
        except ValueError:
            raise abort_transaction("The accout number must be an integer!")
        if acc_num not in self.accounts_dict:
            raise abort_transaction("There is no account " + str(acc_num))
        
        return acc_num
    
#    def ask_for_valid_password(self):
#        password= input("Enter your password:")
        


    def get_user_acc(self):
        acc_num = self.ask_for_valid_acc_num()
        o_acc = self.accounts_dict[acc_num]
        o_acc.check_password_match(acc_num) #ovako oni to imaju u knjizi
        return o_acc
        #o_acc = self.accounts_dict[acc_num]

    def balance(self):
        print("***Get Balance***")
        o_acc = self.get_user_acc()
        the_balance = o_acc.get_balance()
        if the_balance is not None:
            print("Your balance is: ", the_balance)
 
    def create_account(self,the_name,starting_amount,the_password):
        o_acc = Account(the_name,starting_amount,the_password)
        new_acc_num = self.next_acc_num

        self.accounts_dict[new_acc_num] = o_acc

        self.next_acc_num += 1
        return new_acc_num

    def open_acc(self):
        print("***Open Acount***")
        user_name = input("What is the name associated with this account?\n")
        user_starting_amount=int(input("What is the starting balance?\n"))
        user_password = input("Set a password for this account\n")
        user_acc_num = self.create_account(user_name,user_starting_amount,user_password)
        print("Your new account number is: ", user_acc_num)

    def close_acc(self):
        print("***Close Account***")
        user_acc_num=int(input("What is your account number?\n"))
        user_password = input("Enter password please")
        o_acc = self.accounts_dict[user_acc_num]
        the_balance = o_acc.get_balance()
        if the_balance is not None:
            print("You had ", the_balance," in your account, which is being returned to you")

        del self.accounts_dict[user_acc_num]
        print("Your account is now closed")
                

    def deposit(self):
        print("Deposit******")
        o_acc = self.get_user_acc()
        deposit_amount=input("How much would you lke to deposit?")
        the_balance = o_acc.deposit(deposit_amount)
        print("Deposited: ", deposit_amount)
        print("New balance is: ", the_balance)

    def withdraw(self):
        print("Wihdraw*****")
        o_acc = self.get_user_acc()
        user_amount = int(input("How much would you like to withdraw: "))
        the_balance = o_acc.withdraw(user_amount)
        print("Withdrawn: ", user_amount)
        print("New balance is: ", the_balance)

    def get_info(self):
        print("***Get Info***")
        print("Hours: ", self.hours)
        print("Address: ", self.address)
        print("Phone: ", self.phone)
        print("We currently have ", len(self.accounts_dict),' account(s) open')


    def show(self):
        print("***Show***")
        print("This would typically require an admin password")
        for user_acc_num in self.accounts_dict:
            o_account = self.accounts_dict[user_acc_num]
            print("Account: ", user_acc_num)
            o_account.show()
            print()