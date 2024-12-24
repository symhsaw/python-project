"""
Create an expense calculator that have various function
1) Add expense
2) print expenses 
3) print total expenses
4) filter expense by category
5) quit program 

explore the the use lambda function

lambda is same as user-defined function(standalone function)
except that it is anonymous function.

map() applies a function to each item in iterable and returns a lazy iterator
so you need to call it out or force evaluation by consuming the iterator.
e.g force evaluation -> sum() or list()
"""

def add_expense(amount,category,expenses):
    expenses.append({"amount":amount,"category":category})

def print_expense(expenses):
    for expense in expenses:
        print("Expenses",expense)

def total_expense(expenses):
    return sum(map(lambda expense:expense["amount"],expenses))

def filter_expense_category(expenses,user_category):
    return filter(lambda expense:expense["category"]== user_category,expenses)

def main():
    expenses = []

    while True:
        print()
        print("Expense Tracker")
        print("1. Add expense")
        print("2. Print expense")
        print("3. Print total expense")
        print("4. Filter expense by category")
        print("5. Quit")
        
        choice = int(input("Select your choice: "))

        if choice == 1:
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            add_expense(amount,category,expenses)
            print ("You have added Amount:{},Category:{}".format(amount,category))

        elif choice == 2:
            print_expense(expenses)
            

        elif choice == 3:
            total = total_expense(expenses)
            print ("Total expense",total)
    
        elif choice == 4:
            user_category = input("Filter which category?: ")
            filter_category = filter_expense_category(expenses,user_category)
            for category in filter_category:
                print (category)
                
        elif choice == 5:
            print("Program is quitting")
            break
            
main()
