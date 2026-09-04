class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print(f'{self.name} is {self.age} years old')

s1=Student(name="Manasa",age=21)
s1.display()