def add_student():
    name = input("Enter student name: ")
# block
    try:
        with open("students.txt", "a") as file:
                  file.write(name +  "\n")
                  print("student added successfully!")
    except Exception:
        print ("Errror saving student")

def view_students():
    try:
        with open("students.txt", "r") as file:
             data = file.read()
                  
        if data.strip() == "":
               print("No student yet.")
        else:
               print("\n--- students list ---")
               print(data)
    except FileNotFoundError:
         print("No students file found yet.")  
def mark_attendance():
    name = input("Student name: ")
    status = input("Enter status (P/A): ").upper()
    if status =='P':
         record = "PRESENT"
    elif status== "A":
         record = "ABSENT"
    else:
         print("invalid status.")
         return
    try:
          
        with open("attendance.txt", "a") as file:
            file.write(name + " - " + record + "\n")
            print("Attendance recorded successfully!")
    except Exception:
        print("Error recording attendance") 

                      
while True:
    print("\n--- Student System ---")
    print("1. Add Student")
    print("2. View Student")
    print("3. Mark Attendance")
    print("4. Exit")

    choice = input("choose option:")
    if choice == "1":
        add_student()
    elif choice == "2":
       view_students()
    elif choice == "3":
         mark_attendance()
    elif choice == "4":
          print("Good bye!!!") 
          break
    else:
           print("invalid choice.Try again")   
