# Student Report Program

name = input("Enter student name: ")

marks = []

for i in range(5):
    mark = float(input(f"Enter mark for subject {i + 1}: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)

highest = max(marks)
lowest = min(marks)

# Check whether the student passed all subjects
passed = all(m >= 40 for m in marks)

# Calculate grade
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
    grade = "F"

# Display Student Report
print("\n====== STUDENT REPORT ======")
print("Student :", name)
print("Marks   :", marks)
print("Total   :", total)
print("Average :", average)
print("Highest :", highest)
print("Lowest  :", lowest)
print("Grade   :", grade)
print("Result  :", "PASS" if passed else "FAIL")