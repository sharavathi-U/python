# Student Record Management System

students = dict()

def add_student():
    while True:
        name = input('Enter the Name of Student: ')
        if name.isalpha():
            break
        else:
            print("Name should only contain Letters")

    usn = input('Enter the USN: ')

    while True:
        department = input('Enter the Department: ')
        if department.isalpha():
            break
        else:
            print("Department should only contain Letters")


    marks1 = int(input('Enter the Marks of Subject 1: '))
    marks2 = int(input('Enter the Marks of Subject 2: '))
    marks3 = int(input('Enter the Marks of Subject 3: '))

    total = marks1 + marks2 + marks3
    average = total / 3

    working_days = int(input('Enter number of working days: '))
    present_days = int(input('Enter number of days present: '))

    attendance_percentage = 0
    if working_days > 0:
        attendance_percentage = (present_days / working_days) * 100
    elif present_days > working_days:
        print("Present days cannot be greater than working days. Please re-enter.")
    else:
        print('Working days cannot be zero.')
    
        
 
    while True:
        fee_paid = input("Fee Paid (YES/NO): ").upper()
        if fee_paid == "YES" or fee_paid == "NO":
            break
        else:
            print("Please Enter only YES or NO")

    
    students[usn] = {
        "Name": name,
        "Department": department,
        "marks1":marks1,
        "marks2":marks2,
        "marks3":marks3,
        "Total": total,
        "Average": average,
        "Attendance": attendance_percentage,
        "Fee Paid": fee_paid
    }

    print("\nStudent added successfully!\n")

    

    with open('C:\\Users\\DELL\\OneDrive\\python\\myfile.txt','a')as f:
        
        f.write("{:<05} {:<10} {:<05} {:<05} {:<05} {:<05} {:<10} {:<15} {:<20} {:<20}  \n".format(
        name, usn,department,marks1,marks2,marks3, total, average, attendance_percentage,fee_paid))
        f.write("-" * 65 + "\n")

def remove_student():
    usn = input('Enter USN to remove student: ')
    if usn in students:
        removed_data = students.pop(usn)

        print('Student removed successfully.\n')

        # Store removed student details in another file
        with open('C:\\Users\\DELL\\OneDrive\\python\\removed_students.txt', 'a') as f:
            
            f.write("{:<15} {:<15} {:<10} {:<10} {:<10} {:<10} {:<15} {:<20} {:<15} {:<20}\n".format(
                removed_data["Name"],
                usn,
                removed_data["Department"],
                removed_data["marks1"],
                removed_data["marks2"],
                removed_data["marks3"],
                removed_data["Total"],
                removed_data["Average"],
                removed_data["Attendance"],
                removed_data["Fee Paid"]
            ))
            f.write("-" * 80 + "\n")

    else:
        print('Student not found.\n')



def view_student():
    if not students:
        print('No students available.\n')
        return

    for usn, data in students.items():
    
        print("Name:", data["Name"])
        print("USN:", usn)
        print("Department:", data["Department"])
        print("Total:", data["Total"])
        print("Average:", data["Average"])
        print("Attendance:", data["Attendance"])
        print("Fee Paid:", data["Fee Paid"])



while True:
    print("\n--- Student Record Management System ---")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. View Students")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        remove_student()
    elif choice == "3":
        view_student()
    elif choice == "4":
        print("Program Ended")
        break
    else:
        print("Invalid choice. Please try again.")