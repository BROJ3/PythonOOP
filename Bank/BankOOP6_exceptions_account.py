class abort_transaction(Exception):
    pass

class Account():
    def __init__ (self,name,balance,password):
        self.name=name
        self.balance = self.validate_amount(balance)
        self.password = password

    def validate_amount(self,amount):
        try:
            amount= int(amount)
        except ValueError:
            raise abort_transaction("Account number must be an integer")
        if amount <=0:
            raise abort_transaction("Value cant be less than 0")
        return amount
       
    def check_password_match(self,password):
        password = input("WHAT is your password?\n")
        if password != self.password:
            raise abort_transaction("Incorrect password for this account")
        
    def deposit(self,amount_to_deposit):
        amount_to_deposit = self.validate_amount(amount_to_deposit)
        self.balance = self.balance+amount_to_deposit
        return self.balance
    
    def get_balance(self):
        return self.balance
    
    def withdraw(self,amount_to_withdraw):
        amount_to_withdraw = self.validate_amount(amount_to_withdraw)
        if amount_to_withdraw > self.balance:
            raise abort_transaction("You cannot withdraw more than you have in your account")
        self.balance = self.balance - amount_to_withdraw
        return self.balance
    
    #added for debugging
    def show(self):
        print('     Name: ', self.name)
        print('     Balance: ', self.balance)
        print('     Password: ', self.password)
        