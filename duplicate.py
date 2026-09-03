arr = list(map(int, input("Enter the array elements separated by comma: ").split(",")))

duplicates = []

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j] and arr[i] not in duplicates:
            duplicates.append(arr[i])

print("Duplicate values are:", duplicates)