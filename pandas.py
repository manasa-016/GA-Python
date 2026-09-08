import pandas as pd

s = pd.Series([85, 77, 90], index=['Amit', 'Rahul', 'Priya'])
print(s)

df = pd.DataFrame({
    'Name': ['Amit', 'Priya', 'Rahul'],
    'Age': [21, 22, 20],
    'Marks': [85, 92, 78]
})
print(df)

data = {
    'Name': ['Amit', 'Priya', 'Rahul'],
    'Age': [21, 22, 20],
    'Marks': [85, 92, 78]
}

df = pd.DataFrame(data)
print(df)

df = pd.read_csv('students.csv')
print(df.head())

df.to_csv('output.csv', index=False)

df = pd.read_excel('students.xlsx')

df.to_excel('output.xlsx', index=False)