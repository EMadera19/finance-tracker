#Finance Tracker
from tracker import Transaction, Budget
# Importing the Transaction and Budget classes from the tracker.py file.

def main():
    print("Welcome to the Finance Tracker!")
    budget = Budget()  # Create an instance of the Budget class to manage transactions

    while True:
        # Display the main menu options to the user
        print("\nChoose and option:")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. View Total Spent")
        print("4. View Total Income")
        print("5. Exit")

        # Prompt the user to enter their choice
        choice = input("Enter your choice (1-5): ")

        # Process the user's choice

        # Add a new transaction
        if choice == '1':
            name = input("Enter the name of the transaction (e.g., Salary, Groceries): ")
            amount = float(input("Enter the amount for the transaction (positive for income, negative for expense): "))
            category = input("Enter the category of the transaction (e.g., Income, Food, Utilities): ")

            # Create a new Transaction object and add it to the budget
            transaction = Transaction(name, amount, category)
            budget.add_transaction(transaction)

            print(f"Transaction '{name}' added successfully!")

        # View all transactions
        elif choice == '2':
            budget.view_transactions()

        # View total amount spent
        elif choice == '3':
            total_spent = budget.total_spent()
            print(f"Total amount spent: ${total_spent:.2f}")

        # View total income
        elif choice == '4':
            total_income = budget.total_income()
            print(f"Total income: ${total_income:.2f}")

        # Exit the loop and end the program
        elif choice == '5':
            
            print("Exiting the Finance Tracker. Goodbye!")
            break

        # Handle invalid input
        else:
            
            print("Invalid choice. Please try again.")

# Call the main function to run the program
if __name__ == "__main__":
    main()