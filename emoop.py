class Employee:
    def __init__(self,id,name,department,salary):
        self.id=id
        self.name=name
        self.department=department
        self.salary=salary

    def display(self):
        print(f"Employee ID: {self.id}, Name: {self.name}, Department: {self.department}, Salary: {self.salary}")

s1=Employee(id=1,name="Manasa",department="HR",salary=50000)
s1.display()