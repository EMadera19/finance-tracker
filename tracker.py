import datetime

# Transaction class to represent a financial transaction
class Transaction:
    # Initialize a new transaction with the given name, amount, and category.
    def __init__(self, name, amount, category):
        self.name = name # e.g., "Salary", "Groceries"
        self.amount = amount # e.g., 2500 for income or -200 for an expense
        self.category = category # e.g., "Income", "Food", "Utilities"
        self.date = datetime.datetime.now() #Automatically capture the current date and time when the transaction is created

    def __repr__(self):
        # This method returns a string representation of the transaction object.
        return f"Transaction({self.name}, {self.amount}, {self.category}, {self.date.strftime('%Y-%m-%d %H:%M:%S')})"
    
# Budget class to manage a list of transactions
class Budget:

    def __init__(self):
        self.transactions = [] # List to hold all transactions

    def add_transaction(self, transaction):
        self.transactions.append(transaction) # Add a Transaction object to the transactions list

    def view_transactions(self):
        for transaction in self.transactions:
            print(transaction) # Print all transactions in the transactions list

    def total_spent(self):
        return sum(t.amount for t in self.transactions if t.amount < 0) # Return the total amount spent (sum of all negative amounts)

    def total_income(self):
        return sum(t.amount for t in self.transactions if t.amount > 0)  # Return the total amount of income (sum of all positive amounts)
