import mysql.connector


# ============================================
# DATABASE CONNECTION
# ============================================

def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="employee_db"
    )
    return connection


# ============================================
# ADD EMPLOYEE
# ============================================

def add_employee():
    connection = create_connection()
    cursor = connection.cursor()

    print("\n========== ADD EMPLOYEE ==========")

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    department = input("Enter Department: ")
    city = input("Enter City: ")
    salary = float(input("Enter Salary: "))
    login_time = input("Enter Login Time (YYYY-MM-DD HH:MM:SS): ")
    logout_time = input("Enter Logout Time (YYYY-MM-DD HH:MM:SS): ")

    query = """
        INSERT INTO employees
        (name, age, department, city, salary, login_time, logout_time)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        name, age, department, city,
        salary, login_time, logout_time
    )

    cursor.execute(query, values)
    connection.commit()

    print("Employee added successfully.")

    cursor.close()
    connection.close()


# ============================================
# VIEW ALL EMPLOYEES
# ============================================

def view_employees():
    connection = create_connection()
    cursor = connection.cursor()

    print("\n========== ALL EMPLOYEES ==========")

    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    if len(employees) == 0:
        print("No employees found.")
    else:
        for employee in employees:
            print("-----------------------------------")
            print("ID          :", employee[0])
            print("Name        :", employee[1])
            print("Age         :", employee[2])
            print("Department  :", employee[3])
            print("City        :", employee[4])
            print("Salary      :", employee[5])
            print("Login Time  :", employee[6])
            print("Logout Time :", employee[7])

    cursor.close()
    connection.close()


# ============================================
# SEARCH EMPLOYEE
# ============================================

def search_employee():
    connection = create_connection()
    cursor = connection.cursor()

    print("\n========== SEARCH EMPLOYEE ==========")

    employee_id = int(input("Enter Employee ID: "))

    query = "SELECT * FROM employees WHERE id = %s"

    cursor.execute(query, (employee_id,))
    employee = cursor.fetchone()

    if employee:
        print("-----------------------------------")
        print("ID          :", employee[0])
        print("Name        :", employee[1])
        print("Age         :", employee[2])
        print("Department  :", employee[3])
        print("City        :", employee[4])
        print("Salary      :", employee[5])
        print("Login Time  :", employee[6])
        print("Logout Time :", employee[7])
    else:
        print("Employee not found.")

    cursor.close()
    connection.close()


# ============================================
# UPDATE EMPLOYEE
# ============================================

def update_employee():
    connection = create_connection()
    cursor = connection.cursor()

    print("\n========== UPDATE EMPLOYEE ==========")

    employee_id = int(input("Enter Employee ID: "))

    cursor.execute(
        "SELECT * FROM employees WHERE id = %s",
        (employee_id,)
    )

    employee = cursor.fetchone()

    if employee is None:
        print("Employee not found.")
        cursor.close()
        connection.close()
        return

    name = input("Enter New Name: ")
    age = int(input("Enter New Age: "))
    department = input("Enter New Department: ")
    city = input("Enter New City: ")
    salary = float(input("Enter New Salary: "))
    login_time = input("Enter Login Time (YYYY-MM-DD HH:MM:SS): ")
    logout_time = input("Enter Logout Time (YYYY-MM-DD HH:MM:SS): ")

    query = """
        UPDATE employees
        SET name = %s,
            age = %s,
            department = %s,
            city = %s,
            salary = %s,
            login_time = %s,
            logout_time = %s
        WHERE id = %s
    """

    values = (
        name, age, department, city,
        salary, login_time, logout_time,
        employee_id
    )

    cursor.execute(query, values)
    connection.commit()

    print("Employee updated successfully.")

    cursor.close()
    connection.close()


# ============================================
# DELETE EMPLOYEE
# ============================================

def delete_employee():
    connection = create_connection()
    cursor = connection.cursor()

    print("\n========== DELETE EMPLOYEE ==========")

    employee_id = int(input("Enter Employee ID: "))

    cursor.execute(
        "SELECT * FROM employees WHERE id = %s",
        (employee_id,)
    )

    employee = cursor.fetchone()

    if employee is None:
        print("Employee not found.")
    else:
        confirm = input("Are you sure you want to delete? (yes/no): ")

        if confirm.lower() == "yes":
            cursor.execute(
                "DELETE FROM employees WHERE id = %s",
                (employee_id,)
            )

            connection.commit()
            print("Employee deleted successfully.")
        else:
            print("Delete operation cancelled.")

    cursor.close()
    connection.close()


# ============================================
# MAIN MENU
# ============================================

def main():

    while True:

        print("\n====================================")
        print("      EMPLOYEE MANAGEMENT SYSTEM")
        print("====================================")

        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            view_employees()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            update_employee()

        elif choice == "5":
            delete_employee()

        elif choice == "6":
            print("\nThank you for using Employee Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


# ============================================
# RUN PROGRAM
# ============================================

if __name__ == "__main__":
    main()