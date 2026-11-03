# class for students
class Student:
    # constructor
    def __init__(self):
        self.students = {}

    # add students
    def add_student(self):
        try:
            # name validation
            while True:
                name = input('Enter the Name of Student: ')
                if name.isalpha():
                    break
                else:
                    print("Name should only contain Letters")

            usn = input('Enter the USN: ')
            if usn in self.students:
                print("This USN already exists\n")
                return

            # department validation
            while True:
                department = input('Enter the Department: ')
                if department.isalpha():
                    break
                else:
                    print("Department should only contain Letters")

            # marks input
            try:
                marks1 = int(input('Enter the Marks of Subject 1: '))
                marks2 = int(input('Enter the Marks of Subject 2: '))
                marks3 = int(input('Enter the Marks of Subject 3: '))
            except ValueError:
                print("Marks must be numbers only!")
                return

            # total and average
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
            try:
                working_days = int(input('Enter number of working days: '))
                present_days = int(input('Enter number of days present: '))
                if working_days > 0 and present_days <= working_days:
                    attendance_percentage = (present_days / working_days) * 100
                else:
                    print("Invalid attendance input.")
                    attendance_percentage = 0
            except ValueError:
                print("Attendance values must be numbers!")
                attendance_percentage = 0

            # fee status
            while True:
                fee_paid = input("Fee Paid (YES/NO): ").upper()
                if fee_paid in ("YES", "NO"):
                    break
                else:
                    print("Please enter only YES or NO")

            # store student data
            self.students[usn] = {
                "Name": name,
                "Department": department,
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

            # file handling
            try:
                with open('C:\\Users\\DELL\\OneDrive\\python\\myfile.txt', 'a') as f:
                    f.write("{:<15} {:<15} {:<15} {:<10} {:<10} {:<10} {:<10} {:<15} {:<15} {:<15} {:<15}\n"
                            .format(name, usn, department, marks1, marks2, marks3,
                                    total, average, grade, attendance_percentage, fee_paid))
            except FileNotFoundError:
                print("File path not found. Data not saved to file.")

        except Exception as e:
            print("Unexpected error occurred:", e)

    # remove student
    def remove_student(self):
        try:
            usn = input('Enter USN to remove student: ')
            if usn in self.students:
                removed_data = self.students.pop(usn)
                print('Student removed successfully.\n')

                try:
                    with open('C:\\Users\\DELL\\OneDrive\\python\\removed_students.txt', 'a') as f:
                        f.write("{:<15} {:<15} {:<15} {:<10} {:<10} {:<10} {:<15} {:<15} {:<15} {:<15}\n"
                                .format(
                                    removed_data["Name"], usn, removed_data["Department"],
                                    removed_data["marks1"], removed_data["marks2"],
                                    removed_data["marks3"], removed_data["Total"],
                                    removed_data["Average"], removed_data["grade"],
                                    removed_data["Attendance"]
                                ))
                except FileNotFoundError:
                    print("Removed students file path not found.")
            else:
                print('Student not found.\n')
        except Exception as e:
            print("Error while removing student:", e)

    # view students
    def view_student(self):
        try:
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
        except Exception as e:
            print("Error while viewing students:", e)

    # menu
    def menu(self):
        while True:
            try:
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
            except Exception as e:
                print("Menu error:", e)


# create object
obj = Student()
obj.menu()