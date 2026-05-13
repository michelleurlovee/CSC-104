from Account import Account


class SavingsAccount(Account)  :
    def __init__(self, owner, balance=0, intrest_rate=0.02, withdraw_limit=100):
        super().__init__(owner,balance)
        self.intrest_rate = intrest_rate
        self.withdraw_limit = withdraw_limit

    def withdraw(self, amount):
        if amount > self.withdraw_limit:
            print(f"withdraw denied: Savings account limit is ${self.withdraw_limit}.")
            return

        super().withdraw(amount)

    def apply_intrest(self):
        intrest = self.get_balance() * self.intrest_rate
        self.deposit(intrest)      
        print(f"Intrest of ${intrest} applied.")

print("--- Savings Account ---")
savings = SavingsAccount("Alice", 1000)
savings.withdraw(1000)
savings.apply_intrest()  
