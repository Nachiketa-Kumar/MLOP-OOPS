# intiate a class
class employee:
    #speacial initializer method to initialize the attributes of the class or a dunder method
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    #defining a function inside a class is called a method.
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")

sam= employee("Sam", 30, 50000)
sam.display()
print(sam.name)
print(sam.age)
print(sam.salary)
# creating another object of the class
john = employee(input(), int(input()), int(input()))
john.display()
print(john.name)
print(john.age)
print(john.salary)

