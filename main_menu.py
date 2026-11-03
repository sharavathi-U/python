
import my_def as mm
while True:
    print("\n--- Student Record Management System ---")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. View Students")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        mm.add_student()
    elif choice == "2":
        mm.remove_student()
    elif choice == "3":
        mm.view_student()
    elif choice == "4":
        print("Program Ended")
        break
    else:
        print("Invalid choice. Please try again.")