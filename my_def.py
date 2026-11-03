students = {}

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

    # Marks
    marks1 = int(input('Enter the Marks of Subject 1: '))
    marks2 = int(input('Enter the Marks of Subject 2: '))
    marks3 = int(input('Enter the Marks of Subject 3: '))

    total = marks1 + marks2 + marks3
    average = total / 3

    # Attendance
    working_days = int(input('Enter number of working days: '))
    present_days = int(input('Enter number of days present: '))

    attendance_percentage = 0
    if working_days > 0:
        attendance_percentage = (present_days / working_days) * 100
    else:
        print('Working days cannot be zero.')

    # Fee Status
    while True:
        fee_paid = input("Fee Paid (YES/NO): ").upper()
        if fee_paid == "YES" or fee_paid == "NO":
            break
        else:
            print("Please Enter only YES or NO")

    # Store student data in dictionary
    students[usn] = {
        "Name": name,
        "Department": department,
        "Total": total,
        "Average": average,
        "Attendance": attendance_percentage,
        "Fee Paid": fee_paid
    }

   
    
def remove_student():
    usn = input('Enter USN to remove student: ')
    if usn in students:
        students.pop(usn)
        print('Student removed successfully.\n')
    else:
        print('Student not found.\n')


def view_student():
    if not students:
        print('No students available.\n')
        return

    for usn, data in students.items():
        print("\n-----------------------------")
        print("USN:", usn)
        print("Name:", data["Name"])
        print("Department:", data["Department"])
        print("Total:", data["Total"])
        print("Average:", data["Average"])
        print("Attendance:", data["Attendance"])
        print("Fee Paid:", data["Fee Paid"])
        print("-----------------------------")
