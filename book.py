books = [
    {
        "id": 101,
        "title": "Python Basics",
        "author": "John Smith",
        "category": "Programming",
        "price": 500,
        "available": True,
        "issue_count": 0
    },
    {
        "id": 102,
        "title": "Data Structures",
        "author": "Robert Martin",
        "category": "Programming",
        "price": 650,
        "available": True,
        "issue_count": 0
    },
    {
        "id": 103,
        "title": "Wings of Fire",
        "author": "A. P. J. Abdul Kalam",
        "category": "Biography",
        "price": 400,
        "available": True,
        "issue_count": 0
    }
]

students = []

issued_books = []


# ---------------------------------------
# ADD BOOK
# ---------------------------------------

def add_book():

    print("\n========== ADD BOOK ==========")

    book_id = int(input("Enter Book ID: "))

    # Check duplicate ID
    for book in books:
        if book["id"] == book_id:
            print("Book ID already exists.")
            return

    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    category = input("Enter Category: ")
    price = float(input("Enter Book Price: "))

    book = {
        "id": book_id,
        "title": title,
        "author": author,
        "category": category,
        "price": price,
        "available": True,
        "issue_count": 0
    }

    books.append(book)

    print("Book added successfully.")


# ---------------------------------------
# VIEW BOOKS
# ---------------------------------------

def view_books():

    print("\n========== ALL BOOKS ==========")

    if len(books) == 0:
        print("No books available.")
        return

    for book in books:

        print("----------------------------------")
        print("Book ID     :", book["id"])
        print("Title       :", book["title"])
        print("Author      :", book["author"])
        print("Category    :", book["category"])
        print("Price       :", book["price"])

        if book["available"]:
            print("Status      : Available")
        else:
            print("Status      : Issued")


# ---------------------------------------
# SEARCH BOOK BY TITLE
# ---------------------------------------

def search_book_title():
    print("\n========== SEARCH BOOK ==========")

    title = input("Enter book title: ")

    found = False

    for book in books:

        if title.lower() in book["title"].lower():

            print("----------------------------------")
            print("Book ID :", book["id"])
            print("Title   :", book["title"])
            print("Author  :", book["author"])
            print("Category:", book["category"])

            found = True

    if not found:
        print("Book not found.")


# ---------------------------------------
# SEARCH BOOK BY AUTHOR
# ---------------------------------------
def search_book_author():

    print("\n========== SEARCH BY AUTHOR ==========")
    author = input("Enter author name: ")
    found = False
    for book in books:

        if author.lower() in book["author"].lower():

            print("----------------------------------")
            print("Book ID :", book["id"])
            print("Title   :", book["title"])
            print("Author  :", book["author"])
            found = True

    if not found:
        print("No books found.")


# ---------------------------------------
# ADD STUDENT
# ---------------------------------------

def add_student():

    print("\n========== ADD STUDENT ==========")

    student_id = int(input("Enter Student ID: "))

    for student in students:

        if student["id"] == student_id:
            print("Student ID already exists.")
            return

    name = input("Enter Student Name: ")
    course = input("Enter Course: ")
    phone = input("Enter Phone Number: ")

    student = {
        "id": student_id,
        "name": name,
        "course": course,
        "phone": phone
    }

    students.append(student)

    print("Student added successfully.")


# ---------------------------------------
# VIEW STUDENTS
# ---------------------------------------

def view_students():

    print("\n========== ALL STUDENTS ==========")

    if len(students) == 0:
        print("No students registered.")
        return

    for student in students:

        print("----------------------------------")
        print("Student ID :", student["id"])
        print("Name       :", student["name"])
        print("Course     :", student["course"])
        print("Phone      :", student["phone"])


# ---------------------------------------
# SEARCH STUDENT
# ---------------------------------------

def search_student():

    print("\n========== SEARCH STUDENT ==========")

    name = input("Enter student name: ")

    found = False

    for student in students:

        if name.lower() in student["name"].lower():

            print("----------------------------------")
            print("Student ID :", student["id"])
            print("Name       :", student["name"])
            print("Course     :", student["course"])
            print("Phone      :", student["phone"])

            found = True

    if not found:
        print("Student not found.")


# ---------------------------------------
# ISSUE BOOK
# ---------------------------------------

def issue_book():

    print("\n========== ISSUE BOOK ==========")

    student_id = int(input("Enter Student ID: "))
    book_id = int(input("Enter Book ID: "))

    selected_student = None
    selected_book = None

    # Find student
    for student in students:

        if student["id"] == student_id:
            selected_student = student
            break

    if selected_student is None:
        print("Student not found.")
        return

    # Find book
    for book in books:

        if book["id"] == book_id:
            selected_book = book
            break

    if selected_book is None:
        print("Book not found.")
        return

    # Check availability
    if not selected_book["available"]:
        print("Book is already issued.")
        return

    # Check if student already has the book
    for issue in issued_books:

        if issue["student_id"] == student_id:
            if issue["book_id"] == book_id:
                print("This student already has this book.")
                return

    issue = {
        "student_id": student_id,
        "student_name": selected_student["name"],
        "book_id": book_id,
        "book_title": selected_book["title"]
    }

    issued_books.append(issue)

    selected_book["available"] = False
    selected_book["issue_count"] += 1

    print("\nBook issued successfully.")
    print("Student:", selected_student["name"])
    print("Book:", selected_book["title"])


# ---------------------------------------
# RETURN BOOK
# ---------------------------------------

def return_book():

    print("\n========== RETURN BOOK ==========")

    student_id = int(input("Enter Student ID: "))
    book_id = int(input("Enter Book ID: "))

    selected_issue = None

    for issue in issued_books:

        if issue["student_id"] == student_id:
            if issue["book_id"] == book_id:
                selected_issue = issue
                break

    if selected_issue is None:
        print("Issue record not found.")
        return

    # Find book
    for book in books:

        if book["id"] == book_id:
            book["available"] = True
            break

    issued_books.remove(selected_issue)

    print("Book returned successfully.")
    print("Book:", selected_issue["book_title"])


# ---------------------------------------
# VIEW ISSUED BOOKS
# ---------------------------------------

def view_issued_books():

    print("\n========== ISSUED BOOKS ==========")

    if len(issued_books) == 0:
        print("No books are currently issued.")
        return

    for issue in issued_books:

        print("----------------------------------")
        print("Student ID   :", issue["student_id"])
        print("Student Name :", issue["student_name"])
        print("Book ID      :", issue["book_id"])
        print("Book Title   :", issue["book_title"])


# ---------------------------------------
# AVAILABLE BOOKS
# ---------------------------------------

def available_books():

    print("\n========== AVAILABLE BOOKS ==========")

    found = False

    for book in books:

        if book["available"]:

            print("----------------------------------")
            print("ID     :", book["id"])
            print("Title  :", book["title"])
            print("Author :", book["author"])

            found = True

    if not found:
        print("No books available.")


# ---------------------------------------
# DELETE BOOK
# ---------------------------------------

def delete_book():

    print("\n========== DELETE BOOK ==========")

    book_id = int(input("Enter Book ID: "))

    for book in books:

        if book["id"] == book_id:

            if not book["available"]:
                print("Cannot delete an issued book.")
                return

            books.remove(book)

            print("Book deleted successfully.")
            return

    print("Book not found.")


# ---------------------------------------
# MOST ISSUED BOOK
# ---------------------------------------

def most_issued_book():

    print("\n========== MOST ISSUED BOOK ==========")

    if len(books) == 0:
        print("No books available.")
        return

    highest = books[0]

    for book in books:

        if book["issue_count"] > highest["issue_count"]:
            highest = book

    print("Book Title :", highest["title"])
    print("Author     :", highest["author"])
    print("Issued     :", highest["issue_count"], "times")


# ---------------------------------------
# LIBRARY STATISTICS
# ---------------------------------------

def library_statistics():

    print("\n========== LIBRARY STATISTICS ==========")

    total_books = len(books)
    total_students = len(students)
    total_issued = len(issued_books)

    available = 0

    for book in books:

        if book["available"]:
            available += 1

    print("Total Books     :", total_books)
    print("Available Books :", available)
    print("Issued Books    :", total_issued)
    print("Students        :", total_students)


# ---------------------------------------
# CATEGORY REPORT
# ---------------------------------------

def category_report():

    print("\n========== CATEGORY REPORT ==========")

    category_count = {}

    for book in books:

        category = book["category"]

        if category in category_count:
            category_count[category] += 1
        else:
            category_count[category] = 1

    for category, count in category_count.items():

        print(category, ":", count, "books")


# ---------------------------------------
# MAIN MENU
# ---------------------------------------

def main():

    while True:

        print("\n==========================================")
        print("       LIBRARY MANAGEMENT SYSTEM")
        print("==========================================")

        print("1.  Add Book")
        print("2.  View All Books")
        print("3.  Search Book by Title")
        print("4.  Search Book by Author")
        print("5.  Add Student")
        print("6.  View All Students")
        print("7.  Search Student")
        print("8.  Issue Book")
        print("9.  Return Book")
        print("10. View Issued Books")
        print("11. View Available Books")
        print("12. Delete Book")
        print("13. Most Issued Book")
        print("14. Library Statistics")
        print("15. Category Report")
        print("16. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            search_book_title()

        elif choice == "4":
            search_book_author()

        elif choice == "5":
            add_student()

        elif choice == "6":
            view_students()

        elif choice == "7":
            search_student()

        elif choice == "8":
            issue_book()

        elif choice == "9":
            return_book()

        elif choice == "10":
            view_issued_books()

        elif choice == "11":
            available_books()

        elif choice == "12":
            delete_book()

        elif choice == "13":
            most_issued_book()

        elif choice == "14":
            library_statistics()

        elif choice == "15":
            category_report()

        elif choice == "16":
            print("\nThank you for using Library Management System.")
            break

        else:
            print("Invalid choice. Please enter 1-16.")


main()