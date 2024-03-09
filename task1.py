class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
    
    
    def __str__(self):
        return f"You account balance is: {self.balance}"
    
    
    def topup(self, amount):
        self.balance += amount
        return self.balance


account = BankAccount(100)
account.withdraw(50)
account.topup(200)
print(account)



    
    