students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)
        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            print("\nStudents:")
            for student in students:
                print(student)

    elif choice == "3":
        name = input("Enter student name to search: ")

        if name in students:
            print("Student Found!")
        else:
            print("Student Not Found!")

    elif choice == "4":
        name = input("Enter student name to delete: ")

        if name in students:
            students.remove(name)
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    elif choice == "5":
        print("Exiting Student Management System...")
        break

    else:
        print("Invalid choice! Please try again.")
