import numpy as np

arr=np.array([10,20,30,40,50])
print(arr)
print(type(arr))

np.zeros((2,3))
np.ones((2,2))
np.full((3,3),7)
np.arange(1,6)
np.linspace(0,1,5)
np.eye(3)

arr=np.array([10,20,30,40,50])
print(arr[0])
print(arr[-1])
print(arr[1:4])
print(arr[::-1])

print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))
print(np.std(arr))

arr = np.array([10, 20, 30])
print(arr + 5)

arr = np.array([1, 2, 3, 4])

print(arr * 2)
print(np.sqrt(arr))
print(np.power(arr, 2))

arr = np.random.randint(1, 100, 5)
print(arr)
print(np.random.choice(arr))
print(np.random.choice(arr, 3))

arr = np.array([
    [85, 70, 91, 60, 90],
    [71, 80, 70, 75, 78],
    [90, 60, 84, 91, 94]
])

print(np.mean(arr, axis=0))
print(np.max(arr, axis=1))