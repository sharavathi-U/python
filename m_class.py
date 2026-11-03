# class for students
class Student:
    # constructor
    def __init__(self):
        self.students = {}
        self.file_path = 'C:\\Users\\DELL\\OneDrive\\python\\myfile.txt'
        self.removed_file = 'C:\\Users\\DELL\\OneDrive\\python\\removed_students.txt'
        self.write_heading()

    # write heading only once
    def write_heading(self):
        try:
            with open(self.file_path, 'x') as f:
                f.write("STUDENT RECORD MANAGEMENT SYSTEM\n")
                f.write("-" * 120 + "\n")
                f.write("{:<15} {:<15} {:<15} {:<8} {:<8} {:<8} {:<8} {:<10} {:<8} {:<12} {:<10}\n".format(
                    "Name", "USN", "Department", "M1", "M2", "M3",
                    "Total", "Average", "Grade", "Attendance", "Fee Paid"))
                f.write("-" * 120 + "\n")
        except FileExistsError:
            pass

    # add student
    def add_student(self):
        while True:
            name = input('Enter the Name of Student: ')
            if name.isalpha():
                break
            print("Name should only contain letters")

        usn = input('Enter the USN: ')
        if usn in self.students:
            print("This USN already exists\n")
            return

        while True:
            department = input('Enter the Department: ')
            if department.isalpha():
                break
            print("Department should only contain letters")

        # marks
        marks1 = int(input('Enter Marks of Subject 1: '))
        marks2 = int(input('Enter Marks of Subject 2: '))
        marks3 = int(input('Enter Marks of Subject 3: '))

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
        working_days = int(input('Enter working days: '))
        present_days = int(input('Enter days present: '))

        if working_days > 0 and present_days <= working_days:
            attendance = (present_days / working_days) * 100
        else:
            print("Invalid attendance input")
            return

        # fee
        while True:
            fee_paid = input("Fee Paid (YES/NO): ").upper()
            if fee_paid in ("YES", "NO"):
                break
            print("Enter YES or NO only")

        # auto remove condition
        if grade == "Fail":
            print("student is removed due to fail:")
        if attendance < 75:
            print("student is removed due to low attendence")
            self.store_removed(name, usn, department, marks1, marks2, marks3,
                               total, average, grade, attendance, fee_paid)
            return

        # store student
        self.students[usn] = {
            "Name": name,
            "Department": department,
            "marks1": marks1,
            "marks2": marks2,
            "marks3": marks3,
            "Total": total,
            "Average": average,
            "Grade": grade,
            "Attendance": attendance,
            "Fee Paid": fee_paid
        }

        with open(self.file_path, 'a') as f:
            f.write("{:<15} {:<15} {:<15} {:<8} {:<8} {:<8} {:<8} {:<10.2f} {:<8} {:<12.2f} {:<10}\n".format(
                name, usn, department, marks1, marks2, marks3,
                total, average, grade, attendance, fee_paid))

        print("\nStudent added successfully!\n")

    # store removed students
    def store_removed(self, name, usn, dept, m1, m2, m3, total, avg, grade, att, fee):
        with open(self.removed_file, 'a') as f:
            f.write("{:<15} {:<15} {:<15} {:<8} {:<8} {:<8} {:<8} {:<10.2f} {:<8} {:<12.2f} {:<10}\n".format(
                name, usn, dept, m1, m2, m3, total, avg, grade, att, fee))

    # remove student manually
    def remove_student(self):
        usn = input('Enter USN to remove: ')
        if usn in self.students:
            data = self.students.pop(usn)
            self.store_removed(data["Name"], usn, data["Department"],
                               data["marks1"], data["marks2"], data["marks3"],
                               data["Total"], data["Average"], data["Grade"],
                               data["Attendance"], data["Fee Paid"])
            print("Student removed successfully\n")
        else:
            print("Student not found\n")

    # view students
    def view_student(self):
        if not self.students:
            print("No students available\n")
            return

        for usn, data in self.students.items():
            print("\nName:", data["Name"])
            print("USN:", usn)
            print("Department:", data["Department"])
            print("Average:", data["Average"])
            print("Grade:", data["Grade"])
            print("Attendance:", data["Attendance"])
            print("Fee Paid:", data["Fee Paid"])
            print("-" * 40)

    # menu
    def menu(self):
        while True:
            print("\n--- Student Record Management System ---")
            print("1. Add Student")
            print("2. Remove Student")
            print("3. View Students")
            print("4. Exit")

            choice = input("Enter choice: ")

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
                print("Invalid choice")

# create object
if __name__ == '__main__':
   obj = Student()
obj.menu()