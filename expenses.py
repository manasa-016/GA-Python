expenses = []


def add_expense():
    print("\n--- Add Expense ---")

    expense_id = int(input("Enter Expense ID: "))
    description = input("Enter Description: ")
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))

    expense = {
        "id": expense_id,
        "description": description,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)

    print("Expense added successfully!")


def view_expenses():
    print("\n--- All Expenses ---")

    if len(expenses) == 0:
        print("No expenses found.")
        return

    for expense in expenses:
        print("----------------------------")
        print("ID          :", expense["id"])
        print("Description :", expense["description"])
        print("Category    :", expense["category"])
        print("Amount      :", expense["amount"])


def search_by_category():
    print("\n--- Search by Category ---")

    search_category = input("Enter category: ")

    found = False

    for expense in expenses:
        if expense["category"].lower() == search_category.lower():
            print("----------------------------")
            print("ID          :", expense["id"])
            print("Description :", expense["description"])
            print("Amount      :", expense["amount"])

            found = True

    if not found:
        print("No expenses found for this category.")


def calculate_total():
    print("\n--- Total Expense ---")

    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("Total Expense:", total)

def highest_expense():
    print("\n--- Highest Expense ---")

    if len(expenses) == 0:
        print("No expenses found.")
        return

    highest = expenses[0]

    for expense in expenses:
        if expense["amount"] > highest["amount"]:
            highest = expense

    print("Description :",highest['description'])
    print("Category :",highest['category'])
    print("Amount :",highest['amount'])

def delete_expense():
    print("\n--- Delete Expense ---")

    expense_id = int(input("Enter Expense ID to delete: "))

    for expense in expenses:
        if expense['id'] == expense_id:
            expenses.remove(expense)
            print("Expense deleted successfully!")
            return

    print("Expense not found!")

def category_summary():
    print("\n--- Category-Wise Summary ---")

    if len(expenses) == 0:
        print("No expenses found.")
        return

    summary={}

    for expense in expenses:
        category=expense["category"]
        amount=expense["amount"]

        if category in summary:
            summary[category]=summary[category]+amount
        else:
            summary[category]=amount

        for category,amount in summary.items():
            print(category,":",amount)

def main():
    print("\n--- Expense Tracker ---")

    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Search by Category")
        print("4. Calculate Total Expenses")
        print("5. Find Highest Expense")
        print("6. Delete Expense")
        print("7. Category Summary")
        print("8. Exit")

        choice = input("\n Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            search_by_category()

        elif choice == "4":
            calculate_total()

        elif choice == "5":
            highest_expense()
        
        elif choice == "6":
            delete_expense()
        
        elif choice == "7":
            category_summary()
        
        elif choice == "8":
            print("Thank you for using Expense Tracker")
            break

        else:
            print("Invalid choice. Please try again.")

main()



