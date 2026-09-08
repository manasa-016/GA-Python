import numpy as np

marks = np.array([
    [85, 78, 92, 88, 90],
    [72, 80, 75, 70, 78],
    [90, 95, 89, 92, 96],
    [65, 70, 68, 72, 75],
    [88, 84, 91, 86, 89]
])

print(marks)

total = np.sum(marks, axis=1)
print(total)

average = np.mean(marks, axis=1)
print(average)

highest = np.max(marks, axis=1)
print(highest)

lowest = np.min(marks, axis=1)
print(lowest)

subject_average = np.mean(marks, axis=0)
print(subject_average)

average = np.mean(marks, axis=1)
selected_students = average > 75
print(selected_students)

std = np.std(marks, axis=1)
print(std)

average = np.mean(marks, axis=1)
top_student_index = np.argmax(average)
print("Top Student Index:", top_student_index)
print("Top Student Average:", average[top_student_index])