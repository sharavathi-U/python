# Parent class
class Person:
    def __init__(self):
        self.name = ""
        self.usn = ""
        self.department =""

    def details(self):
        while True:
            self.name = input('Enter the Name of Student: ')
            if self.name.isalpha():
                break
            else:
                print("Name should only contain Letters")

        self.usn = input('Enter the USN: ')

        while True:
            self.department = input('Enter the Department: ')
            if self.department.isalpha():
                break
            else:
                print("Department should only contain Letters")


# Child class (Inheritance)
class Student(Person):

    def __init__(self):
        super().__init__()   # calling parent constructor
        self.students = {}

    def add_student(self):
        self.details()

        if self.usn in self.students:
            print("This USN already exists\n")
            return

        # marks
        marks1 = int(input('Enter the Marks of Subject 1: '))
        marks2 = int(input('Enter the Marks of Subject 2: '))
        marks3 = int(input('Enter the Marks of Subject 3: '))

        total = marks1 + marks2 + marks3
        average = total / 3

        # grade calculation
        if average >= 90:
            grade = "A+"
        elif average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        else:
            grade = "Fail"

        # attendance
        working_days = int(input('Enter number of working days: '))
        present_days = int(input('Enter number of days present: '))

        if working_days > 0 and present_days <= working_days:
            attendance_percentage = (present_days / working_days) * 100
        else:
            print("Invalid attendance input.")
            attendance_percentage = 0

        while True:
            fee_paid = input("Fee Paid (YES/NO): ").upper()
            if fee_paid in ("YES", "NO"):
                break
            else:
                print("Please Enter only YES or NO")

        self.students[self.usn] = {
            "Name": self.name,
            "Department": self.department,
            "marks1": marks1,
            "marks2": marks2,
            "marks3": marks3,
            "Total": total,
            "Average": average,
            "grade": grade,
            "Attendance": attendance_percentage,
            "Fee Paid": fee_paid
        }

        print("\nStudent added successfully!\n")

        with open('C:\\Users\\DELL\\OneDrive\\python\\myfile.txt', 'a') as f:
            f.write("{:<15} {:<15} {:<15} {:<10} {:<10} {:<10} {:<10} {:<15} {:<15} {:<15} {:<15}\n".format(
                self.name, self.usn, self.department,
                marks1, marks2, marks3,
                total, average, grade,
                attendance_percentage, fee_paid))
            print("---------Student Record Management System------------")

    def remove_student(self):
        usn = input('Enter USN to remove student: ')
        if usn in self.students:
            removed_data = self.students.pop(usn)

            print('Student removed successfully.\n')

            with open('C:\\Users\\DELL\\OneDrive\\python\\removed_students.txt', 'a') as f:
                f.write("{:<15} {:<15} {:<15} {:<10} {:<10} {:<10} {:<15} {:<15} {:<15} {:<15}\n".format(
                    removed_data["Name"],
                    usn,
                    removed_data["Department"],
                    removed_data["marks1"],
                    removed_data["marks2"],
                    removed_data["marks3"],
                    removed_data["Total"],
                    removed_data["Average"],
                    removed_data["grade"],
                    removed_data["Attendance"],
                    removed_data["Fee Paid"]
                ))
        else:
            print('Student not found.\n')

    def view_student(self):
        if not self.students:
            print('No students available.\n')
            return

        for usn, data in self.students.items():
            print("\nName:", data["Name"])
            print("USN:", usn)
            print("Department:", data["Department"])
            print("Total:", data["Total"])
            print("Average:", data["Average"])
            print("Grade:", data["grade"])
            print("Attendance:", data["Attendance"])
            print("Fee Paid:", data["Fee Paid"])
            print("-" * 40)

    def menu(self):
        while True:
            print("\n--- Student Record Management System ---")
            print("1. Add Student")
            print("2. Remove Student")
            print("3. View Students")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.remove_student()
            elif choice == "3":
                self.view_student()
            elif choice == "4":
                print("Program Ended")
                break
            else:
                print("Invalid choice. Please try again.")


# Create object
obj = Student()
obj.menu()