class Account():
    owner = ""
    balance = 0
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    
    def __str__(self):
        return f"Аккаунт принадлежит: {self.owner}\nБаланс на аккаунте: {self.balance}"
    
    def deposit(self, count):
        self.balance += count
        return f"Deposited: {count}\nДоступная сумма: {self.balance}"
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Снятие произведено: {amount}\nДоступная сумма: {self.balance}"
        else: 
            return f"Операция невозможна, ваш баланс -> {self.balance}"
        

acc1 = Account("Aibyn", 5000)
print(acc1)
print(acc1.deposit(500))
print(acc1.withdraw(2000))
print(acc1.balance)


