def date():
    date =input("YYYY-MM-DD: ")
    try:
        with open("expense.txt", "a") as file:
               file.write(date +"\n")
        user_input = int(date)
        print(f"you entered an invalid date: {user_input}")
    except ValueError:
        print("Invalid input.Please enter a date")
def Amount():
    Amount = input("Enter a number: ")
    try:
       with open("expense.txt", "a") as file:
          file.write(date + Amount +"\n")
          user_input = int(Amount)
          print(f"you entered an integer: {user_input}")
    except ValueError:
         print("Invalid input.Please enter a whole number.")
def add_expense():
    expense =input("date","Amount")
    try:
        with open("expense.txt", "a") as file:
            file.write(date + Amount + "\n")
            print("expense added successfully")
    except Exception:
            print("Error saving expense")    
def view_expense():
    try:
        with open("expense.txt", "r") as file:
          data = file.read()

        if data.strip() == "":
          print("No expense yet.")
        else:
          print("\n---expense list---")
          print(data)
    except FileNotFoundError:
          print("No expense file found yet.")
def total_expense():
    expense = input("expense")
     
    status = input("Enter status (F/T/B): ").lower()
    if status == "F":
                record = "Food"
    elif status == "T":
                record = "Transport"
    elif status == "B":
                record = "Bills"
    else:
                print("invalid status")
    return
    try:
        with open("expense.txt", "a") as file:
         file.write(add_expense + "-" + record +"\n")
         print("Expense recorded successfully")
    except Exception:
            print("Error recording expense")

while True:
     print("\n---Expense Tracker---")
     print("1. date")
     print("2. Amount")
     print("3. add expense")
     print("4. view expense")
     print("5. total expense")
     print("6. Exit")

     choice = input("choose option:")
     if choice == "1":
        date()
     elif choice == "2":
         Amount()
     elif choice == "3":
          add_expense
     elif choice =="4":
         view_expense()
     elif choice =="5":
        total_expense
     elif choice =="6":
         print("Goodbye!!!")
     else:
        print("invalid choice.Try again")
    
        