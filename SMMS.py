# 1. List - Store student names
students = ["Rahul", "Priya", "Amit", "Sneha", "Ravi"]

# 2. Tuple - Store subjects
subjects = ("Python", "Java", "SQL")

# 3. Dictionary - Store marks of each student
marks = {
    "Rahul": [80, 75, 85],
    "Priya": [90, 85, 88],
    "Amit": [70, 65, 75],
    "Sneha": [85, 80, 90],
    "Ravi": [75, 70, 80]
}

# 4. Set - Store unique student names
unique_students = set(students)

print("Student Marks Management System")
print("--------------------------------")

print("\nStudents:")
print(students)

print("\nSubjects:")
print(subjects)

# Variables to find top student
highest_total = 0
top_student = ""

# Display student details
for student in students:

    print("\n" + student)

    student_marks = marks[student]

    # Display subject-wise marks
    for i in range(len(subjects)):
        print(subjects[i], ":", student_marks[i])

    # Calculate total
    total = sum(student_marks)

    # Calculate average
    average = total / len(subjects)

    print("Total:", total)
    print("Average:", round(average, 2))

    # Find highest scorer
    if total > highest_total:
        highest_total = total
        top_student = student

# Display top student
print("\n--------------------------------")
print("Top Student:", top_student)
print("Highest Total:", highest_total)

# Display unique students
print("\nUnique Students:")
print(unique_students)