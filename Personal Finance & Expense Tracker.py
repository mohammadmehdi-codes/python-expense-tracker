import json
from datetime import datetime
expense_list = []
   
def save_file():
    with open("expense_dump.json","w")as f:
        json.dump(expense_list,f)

def load_file():
    global expense_list
    try:
        with open("expense_dump.json","r") as f:
            expense_list = json.load(f) 
    except (FileNotFoundError, json.JSONDecodeError):
        expense_list = []
        print("No previous expense data found.")              

def add_expense():
    c = input("Enter your expense category: ").strip()
    c = c.upper()
    if not c:
        print("Empty category not allowed")
        return
    elif not c.replace(" ","").isalpha():
        print("Only Alphabet allowed")
        return
    else:
        try:
            a = float(input("Enter your expense amount: "))
            if a <= 0:
                print("only positive value allowed")
                return
        except ValueError:
            print("Invalid input.")
            return 
    try:
        d = input("please enter date (DD-MM-YYYY)").strip()
        datetime.strptime(d, "%d-%m-%Y")
    except ValueError:
        print("Invalid date. Please use DD-MM-YYYY.")
        return
    
    expenses = {
        "category" : c,
        "amount" : a,
        "date" : d,
    }            
    expense_list.append(expenses)
    print("Expense added successfully.")
    save_file()

def view_all_expenses():
    if not expense_list:
        print("No item found")
    else:
        for x, i in enumerate (expense_list, start=1):
            print(x, ":", i["category"], "|", f'{i["amount"]:.2f}', "|", i["date"])

def view_total_expenses():
    if not expense_list:
        print("No item found for calculation")
    else:
        total = 0
        for x in expense_list:
            total = x["amount"] + total
        print(f"Total expenses are: {total:.2f}")

def delete_expense():
    if not expense_list:
        print("No expense found")
    else:
        for i,x in enumerate(expense_list, start=1):
            print(i, ":", x["category"], "|", f'{x["amount"]:.2f}', "|", x["date"])
        try:
            delete = int(input("Which serial no expense want to delete: "))
        except ValueError:
            print("Invalid input.")
            return
        if delete > len(expense_list) or delete <= 0:
            print("invalid input.")
            return 
        del expense_list[delete-1]
        print("Deleted, updated list given.")
        save_file()
        if not expense_list:
            print("No expense found")
        else:
            for i,x in enumerate(expense_list, start=1):
                print(i, ":", x["category"], "|", f'{x["amount"]:.2f}', "|", x["date"]) 

def monthly_report():
    month = input("Please enter month: ")
    try:    
        temp_month = int(month)
    except ValueError:
        print("Please follow correct format.")
        return
    if temp_month > 0 and temp_month < 13:
        year = input("Please enter year: ")
        if len(year) == 4 and year.isdigit() :
            print("Monthly expense report: ",month,"|",year,)
            print("------------------------------------") 
            total = 0
            found = False
            for x in expense_list:
                parts = x["date"].split("-")
                m = parts[1]
                y = parts[2]    
                if month == m and year == y:
                    found = True
                    print(x["category"], "|", f'{x["amount"]:.2f}')
                    total = x["amount"] + total
            if not found:
                print("No expenses found for this month.")
            print("------------------------------------")        
            print(f"Total expense on this month:  {total:.2f}")
        else:
            print("Please enter year in correct format")   
    else:
        print("Please enter month in correct format")

def cat_report():
    cx = input("enter category: ").strip()
    if not cx:
        print("only space not allowed")
    else:
        c = cx.upper()
        total = 0
        found = False
        print("Category wise report:",c)
        print("------------------------------------")
        for x in expense_list:
            if c == x["category"]:
                found = True
                print(f'{x["amount"]:.2f}', "|", x["date"])
                total = x["amount"] + total
        if not found:
            print("No expense found on this category.")
        print("------------------------------------")        
        print(f"Total expense in this category: {total:.2f}")            

def all_cat_report():
    if not expense_list:
        print("No data available.")
    else:
        categories = []
        print("All Category expenses:-")
        print("------------------------------------")
        for x in expense_list:
            categories.append(x["category"])
        u_cat = set(categories)
        for x in u_cat:
            total = 0
            for i in expense_list:
                if i["category"] == x:
                    total = i["amount"] + total
            print("Overall",x,f"expenses: {total:.2f}")
        print("------------------------------------")
        grand_total = 0
        for x in expense_list:
            grand_total = x["amount"] + grand_total
        print(f"Grand Total: {grand_total:.2f}")
            
load_file()
while True:
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Delete Expense")
    print("5. Reports")
    print("6. Exit")

    try:
        user = int(input("Choose between 1 to 6: "))
    except ValueError:
        print("only 1 to 6 allowed")
        continue
    if user == 1:
        add_expense()
    elif user ==2:
        view_all_expenses()
    elif user == 3:
        view_total_expenses()
    elif user == 4:
        delete_expense()
    elif user == 5:
        print("1. Monthly report")
        print("2. Category wise report")
        print("3. All category report")
        try:
            user1 = int(input("Choose between 1 to 3: "))
        except ValueError:
            print("only 1 to 3 allowed")
            continue
        if user1 == 1:
            monthly_report()
        elif user1 == 2:
            cat_report()
        elif user1 == 3:
            all_cat_report()  
        else:
            print("invalid input.")
    elif user == 6:
        print("Thankyou!")
        break    
    else:
        print("Invalid Input.")       
