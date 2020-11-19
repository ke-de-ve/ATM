class Account:
    def __init__(self, name, acc_number, balance, pin):
        self.name = name
        self.acc_number = acc_number
        self.balance = balance
        self.pin = pin
    
    def deposit(self, sum_to_deposit):
        self.balance += sum_to_deposit
    
    def withdraw(self, sum_to_withdraw):
        self.balance -= sum_to_withdraw

    def auth(self, pin):
        return (self.pin == pin)

    def check_balance(self):
        print(self.balance)