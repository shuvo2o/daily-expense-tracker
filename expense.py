# Daily expense tracker program
expenses = []
def add_expenses(description, amount):
    expenses.append({"description": description, "amount":amount})
    
def view_expenses():
    for expense in expenses:
        print(f"{expense['description']}: ${expense['amount']}")
        
def total_expenses():
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total Expenses: ${total}")
    
add_expenses("Lunch", 95.80)
add_expenses("Dinner", 20.80)
view_expenses()


total_expenses()
