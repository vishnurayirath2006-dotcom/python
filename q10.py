class BankAccount:
    def __init__(self, account_number, account_holder_name, account_type, initial_balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_type = account_type
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def display_account_details(self):
        print("Account Number:", self.account_number)
        print("Account Holder Name:", self.account_holder_name)
        print("Account Type:", self.account_type)
        print("Current Balance:", self.balance)


account_number = input("Enter account number: ")
account_holder_name = input("Enter account holder name: ")
account_type = input("Enter account type: ")
initial_balance = float(input("Enter initial balance: "))

account = BankAccount(
    account_number,
    account_holder_name,
    account_type,
    initial_balance
)

account.display_account_details()

deposit_amount = float(input("Enter deposit amount: "))
account.deposit(deposit_amount)

withdraw_amount = float(input("Enter withdrawal amount: "))
account.withdraw(withdraw_amount)

print("\nUpdated account details:")
account.display_account_details()