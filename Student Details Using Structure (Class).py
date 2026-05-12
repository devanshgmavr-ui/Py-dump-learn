class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print(f"Name   : {self.name}")
        print(f"Roll No: {self.roll}")
        print(f"Marks  : {self.marks}")

name = input("Enter student name  : ")
roll = int(input("Enter roll number   : "))
marks = float(input("Enter marks         : "))

s = Student(name, roll, marks)

print("\n--- Student Record ---")
s.display()