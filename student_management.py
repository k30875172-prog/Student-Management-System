students = []

def add_student():
    name = input("Enter student name: ")
    marks = float(input("Enter student marks: "))

    student = {
        "name": name,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found!")
    else:
        for student in students:
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            print("----------------")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
