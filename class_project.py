# class for students
class Student:
#constructor
    def __init__(self):
        self.students = {}
# add students
    def add_student(self):
        while True:
            name = input('Enter the Name of Student: ')
            if name.isalpha():
                break
            else:
                print("Name should only contain Letters")

        usn = input('Enter the USN: ')
        if usn in self.students:
            print("this usn already exits\n")
            return
            
        while True:
            department = input('Enter the Department: ')
            if department.isalpha():
                break
            else:
                print("Department should only contain Letters")
   # marks
        marks1 = int(input('Enter the Marks of Subject 1: '))
        marks2 = int(input('Enter the Marks of Subject 2: '))
        marks3 = int(input('Enter the Marks of Subject 3: '))
    # average of marks
        total = marks1 + marks2 + marks3
        average = total / 3
    
    # Grade calculation
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
    
    #checking attendence
        working_days = int(input('Enter number of working days: '))
        present_days = int(input('Enter number of days present: '))

        if working_days > 0 and present_days <= working_days:
            attendance_percentage = (present_days / working_days) * 100
        else:
            print("Invalid attendance input.")
            attendance_percentage = 0

        while True:
            fee_paid = input("Fee Paid (YES/NO): ").upper()
            if fee_paid == "YES" or fee_paid == "NO":
                break
            else:
                print("Please Enter only YES or NO")
#store student data in a file
        self.students[usn] = {
            "Name": name,
            "Department": department,
            "marks1":marks1,
            "marks2":marks2,
            "marks3":marks3,
            "Total": total,
            "Average": average,
            "grade" :grade,
            "Attendance": attendance_percentage,
            "Fee Paid": fee_paid
        }

        print("\nStudent added successfully!\n")

        with open('C:\\Users\\DELL\\OneDrive\\python\\myfile.txt', 'a') as f:
            f.write("{:<15} {:<15} {:<15} {:<10} {:<10} {:<10} {:<10} {:<15} {:<15} {:<15} {:<15}\n".format(
                name, usn, department,marks1,marks2,marks3 ,total, average,grade, attendance_percentage,fee_paid))
            
# remove students stored in another file
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
# view all students 
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
            print("grade:",data["grade"])
            print("Attendance:", data["Attendance"])
            print("Fee Paid:", data["Fee Paid"])
            print("-" * 40)
 # creating menu for student class
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