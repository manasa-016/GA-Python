fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [10, 20, 30, 40])
ax.set_title('Simple Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
plt.show()

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [170, 150, 180, 140, 220]

plt.plot(months, sales, marker='o',
         color='blue', linestyle='-')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

subjects = ['Python', 'Java', 'C++', 'SQL']
marks = [90, 80, 85, 82]

plt.bar(subjects, marks, color=['blue', 'orange', 'green', 'red'])
plt.title('Subject-wise Marks')
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.show()


study_hours = [1, 2, 3, 4, 5, 6]
marks = [35, 50, 55, 65, 75, 90]

plt.scatter(study_hours, marks, color='purple')
plt.title('Study Hours vs Marks')
plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.show()

marks = [45, 50, 52, 55, 60, 62, 65, 68, 70,
         72, 75, 78, 80, 82, 85, 88, 90, 92, 95]

plt.hist(marks, bins=5,
         color='skyblue', edgecolor='black')
plt.title('Distribution of Marks')
plt.xlabel('Marks')
plt.ylabel('Number of Students')
plt.show()


departments = ['CS', 'IT', 'Mechanical', 'Civil']
students = [40, 30, 20, 10]

plt.pie(students, labels=departments,
        autopct='%1.1f%%', startangle=90,
        colors=['blue', 'orange', 'red', 'skyblue'])
plt.title('Students by Department')
plt.show()

# Example dataset
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [120000, 150000, 180000, 140000, 220000, 250000]
expenses = [80000, 90000, 100000, 95000, 120000, 130000]
profit = [40000, 60000, 80000, 45000, 100000, 120000]

# Create charts (line, bar, pie, etc.)
# Save charts
plt.savefig('sales_report.png')