# Expense Tracker Project

expenses = []   # List to store expenses
print("\n Welcome to Expense Tracker : kharcha kam kiya karo dude.....")

while True:
    print("\n--------MENU-------")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice = input("\n Please Enter your choice (1-4): ")

    # Add Expenses
    if choice == "1":

        date = input("\n Enter the expense date (DD/MM/YYYY): ")
        category = input("\n Enter the expense category (Food, Travel, Makeup, Books): ")

        # Error handling for amount
        try:
            amount = float(input("\n Enter the expense amount: "))
        except ValueError:
            print("Invalid amount! Please enter numbers only.")
            continue

        description = input("\n Enter the expense description: ")

        expense = {
            "date": date,
            "category": category,
            "amount": amount,
            "description": description
        }

        expenses.append(expense)

        print("\n Done Dude :) Expense added successfully!")

    # View All Expenses
    elif choice == "2":

        if len(expenses) == 0:
            print("No expenses found.")

        else:
            print("\n All Expenses:")

            for idx, expense in enumerate(expenses, start=1):

                print(
                    f"{idx}. Date: {expense['date']}, "
                    f"Category: {expense['category']}, "
                    f"Amount: {expense['amount']}, "
                    f"Description: {expense['description']}"
                )

    # View Total Expenses
    elif choice == "3":

        total_expenses = sum(expense['amount'] for expense in expenses)

        print(f"\nTotal Expenses: {total_expenses}")
        print("Try to save more money!")

    # Exit
    elif choice == "4":

        print("Exiting the Expense Tracker. Goodbye Dude! \n")
        break

    # Invalid Choice
    else:

        print("Invalid choice. Please enter a number between 1 and 4. \n")