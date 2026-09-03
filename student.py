import mysql.connector

# ============================================
# DATABASE CONNECTION
# ============================================

def create_connection():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="student_db"
    )

    return connection


# ============================================
# CREATE - ADD STUDENT
# ============================================
def add_student():
    connection = create_connection()
    cursor = connection.cursor()

    print("\n========== ADD STUDENT ==========")

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    city = input("Enter City: ")
    marks = float(input("Enter Marks: "))

    query = """
        INSERT INTO students
        (name, age, course, city, marks)
        VALUES (%s, %s, %s, %s, %s)
    """

    values = (name, age, course, city, marks)

    cursor.execute(query, values)
    connection.commit()

    print("Student added successfully.")
    cursor.close()
    connection.close()

def view_students():
    connection = create_connection()
    cursor = connection.cursor()
    print("\n========== ALL STUDENTS ==========")
    query = "SELECT * FROM students"
    cursor.execute(query)
    students = cursor.fetchall()
    if len(students) == 0:
        print("No students found.")
    else:
        for student in students:
            print("-----------------------------------")
            print("ID      :", student[0])
            print("Name    :", student[1])
            print("Age     :", student[2])
            print("Course  :", student[3])
            print("City    :", student[4])
            print("Marks   :", student[5])

    cursor.close()
    connection.close()

def search_student():
    connection = create_connection()
    cursor = connection.cursor()
    print("\n========= SEARCH STUDENT =========")
    student_id = int(input("Enter Student ID: "))

    # SQL query to search for a student by ID
    query = "SELECT * FROM students WHERE id = %s"
    cursor.execute(query, (student_id,))
    # Fetch the result
    student = cursor.fetchone()
    if student:
        print("---------------------------------")
        print("ID      :", student[0])
        print("Name    :", student[1])
        print("Age     :", student[2])
        print("Course  :", student[3])
        print("City    :", student[4])
        print("Marks   :", student[5])
    else:
        print("Student not found.")
    # Close database resources
    cursor.close()
    connection.close()

def update_student():
    connection = create_connection()
    cursor = connection.cursor()
    print("\n========== UPDATE STUDENT ==========")
    student_id = int(input("Enter Student ID: "))
    # Check student exists
    query = "SELECT * FROM students WHERE id = %s"
    cursor.execute(query, (student_id,))
    student = cursor.fetchone()
    if student is None:
        print("Student not found.")
        cursor.close()
        connection.close()
        return
    print("\nCurrent Details")
    print("Name   :", student[1])
    print("Age    :", student[2])
    print("Course :", student[3])
    print("City   :", student[4])
    print("Marks  :", student[5])
    print("\nEnter New Details")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    city = input("Enter City: ")
    marks = float(input("Enter Marks: "))
    query = """
    UPDATE students
    SET name = %s,
        age = %s,
        course = %s,
        city = %s,
        marks = %s
    WHERE id = %s
    """
    values=(name,age,course,city,marks,student_id)
    cursor.execute(query,values)
    connection.commit()
    print("Student updated successfully")
    cursor.close()
    connection.close()

def delete_student():
    connection = create_connection()
    cursor = connection.cursor()
    print("\n========= DELETE STUDENT =========")
    student_id = int(input("Enter Student ID: "))
    # Check student exists
    query = "SELECT * FROM students WHERE id = %s"
    cursor.execute(query, (student_id,))
    student = cursor.fetchone()

    if student is None:
        print("Student not found.")
        cursor.close()
        connection.close()
        return
    print("Student Name:", student[1])
    confirm = input("Are you sure you want to delete? (yes/no): ")
    if confirm.lower() == "yes":
        query = "DELETE FROM students WHERE id = %s"
        cursor.execute(query, (student_id,))
        connection.commit()
        print("Student deleted successfully.")
    else:
        print("Delete operation cancelled.")
    cursor.close()
    connection.close()
# =================================
# SEARCH BY COURSE
# =================================
def search_by_course():
    connection = create_connection()
    cursor = connection.cursor()
    print("\n========== SEARCH BY COURSE ==========")
    course = input("Enter Course: ")
    query = """
        SELECT * FROM students
        WHERE course = %s
    """
    cursor.execute(query, (course,))
    students = cursor.fetchall()
    if len(students) == 0:
        print("No students found.")
    else:
        for student in students:
            print("------------------------------------")
            print("ID      :", student[0])
            print("Name    :", student[1])
            print("Age     :", student[2])
            print("Course  :", student[3])
            print("City    :", student[4])
            print("Marks   :", student[5])
    cursor.close()
    connection.close()

def top_student():
    connection = create_connection()
    cursor = connection.cursor()

    print("\n========== TOP STUDENT ==========")

    query = """
        SELECT * FROM students
        ORDER BY marks DESC
        LIMIT 1
    """

    cursor.execute(query)
    student = cursor.fetchone()

    if student:
        print("Student ID:", student[0])
        print("Name      :", student[1])
        print("Age       :", student[2])
        print("Course    :", student[3])
        print("City      :", student[4])
        print("Marks     :", student[5])

    else:
        print("No students found.")

    cursor.close()
    connection.close()

# ================================================

def student_count():
    connection = create_connection()
    cursor = connection.cursor()

    print("\n========== STUDENT COUNT ==========")

    query = "SELECT COUNT(*) FROM students"

    cursor.execute(query)

    result = cursor.fetchone()

    print("Total Students:", result[0])

    cursor.close()
    connection.close()


# ================================================
# MAIN MENU
# ================================================

def main():
    while True:

        print("\n")
        print("==========================================")
        print("       STUDENT MANAGEMENT SYSTEM")
        print("==========================================")

        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Search by Course")
        print("7. Find Top Student")
        print("8. Student Count")
        print("9. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":

            delete_student()

        elif choice == "6":

            search_by_course()

        elif choice == "7":

            top_student()

        elif choice == "8":

            student_count()

        elif choice == "9":

            print("\nThank you for using Student Management System.")

            break

        else:

            print("Invalid choice. Please try again.")
            
main()