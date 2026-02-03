def date():
    date_input =input("YYYY-MM-DD: ")
    try:
        with open("expense.txt", "a") as file:
               file.write(date_input +"\n")
        print(f"Date entered: {date_input}")
    except ValueError:
        print("Invalid input.Please enter a date")
def Amount():
    amount_input = input("Enter a number: ")
    try:
       user_input = int(amount_input)
       with open("expense.txt", "a") as file:
          file.write(amount_input +"\n")
          print(f"you entered an integer: {user_input}")
    except ValueError:
         print("Invalid input.Please enter a whole number.")
def add_expense():
    date_input = input("Enter date (YYYY-MM-DD): ")
    amount_input = input("Enter amount: ")
    try:
        with open("expense.txt", "a") as file:
            file.write(date_input + " - " + amount_input + "\n")
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
    expense = input("Enter expense amount: ")
     
    status = input("Enter status (F/T/B): ").lower().strip()
    if status == "f":
                record = "Food"
    elif status == "t":
                record = "Transport"
    elif status == "b":
                record = "Bills"
    else:
                print("invalid status")
                return
    try:
        with open("expense.txt", "a") as file:
         file.write(expense + "-" + record +"\n")
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
          add_expense()
     elif choice =="4":
         view_expense()
     elif choice =="5":
        total_expense()
     elif choice =="6":
         print("Goodbye!!!")
         break
     else:
        print("invalid choice.Try again")
    
        