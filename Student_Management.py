print("Welcome to the Student Data Organizer")
print("")

students = []

while True:
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            print("\nEnter student details:")

            student_id = int(input("Student ID: "))
            name = input("Name: ")
            age = int(input("Age: "))
            grade = input("Grade: ")
            dob = input("Date of Birth (YYYY-MM-DD): ")
            subjects = input("Subjects (comma-separated): ")

            student = {"Student ID": student_id, "Name": name,"Age": age,"Grade": grade,"Date of Birth": dob, "Subjects": subjects }

            students.append(student)

            print("\nStudent added successfully!")

        case 2:
            print("\n--- Display All Students ---")

            if len(students) == 0:
                print("No students found.")
            else:
                for student in students:
                    print("Student ID:", student["Student ID"],"| Name:", student["Name"],"| Age:", student["Age"],
                          "| Grade:", student["Grade"], "| Subjects:", student["Subjects"]
                    )

        case 3:
            student_id = int(input("\nEnter Student ID to update: "))

            for student in students:
                if student["Student ID"] == student_id:

                    print("\nStudent found!")

                    student["Name"] = input("Enter new Name: ")
                    student["Age"] = int(input("Enter new Age: "))
                    student["Grade"] = input("Enter new Grade: ")
                    student["Date of Birth"] = input(
                        "Enter new Date of Birth (YYYY-MM-DD): "
                    )
                    student["Subjects"] = input(
                        "Enter new Subjects (comma-separated): "
                    )

                    print("Student information updated successfully!")
                    break

            else:
                print("Student not found.")

        case 4:
            student_id = int(input("\nEnter Student ID to delete: "))

            for student in students:
                if student["Student ID"] == student_id:

                    students.remove(student)
                    print("Student deleted successfully!")
                    break

            else:
                print("Student not found.")

        case 5:
            print("\nSubject Offered:")
            print("- Mathematics")
            print("- Science")
            print("- English")
            print("- History")

        case 6:
            print("\nThank You !!")
            break

        case _:
            print("Invalid choice!")