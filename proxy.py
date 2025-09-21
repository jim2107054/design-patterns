# Subject Interface
class BankAccount:
    def withdraw(self, amount):
        pass


# Real Subject
class RealBankAccount(BankAccount):
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdraw {amount}, Remaining balance = {self.balance}"
        else:
            return "Not enough balance!"


# Proxy
class BankAccountProxy(BankAccount):
    def __init__(self, real_account, user_role):
        self.real_account = real_account
        self.user_role = user_role

    def withdraw(self, amount):
        if self.user_role != "admin":
            return "Access Denied: You are not allowed!"
        return self.real_account.withdraw(amount)


# Client Code
if __name__ == "__main__":
    real_account = RealBankAccount(1000)

    proxy_admin = BankAccountProxy(real_account, "admin")
    proxy_guest = BankAccountProxy(real_account, "guest")

    print(proxy_admin.withdraw(200))   # Allowed
    print(proxy_guest.withdraw(200))   # Denied
