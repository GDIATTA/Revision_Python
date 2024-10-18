class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print("Hello my name is " + self.name)

class Student(Person):
    def __init__(self,name,age):
        #Person.__init__(self,name,age)
        super().__init__(name,age)
        self.graduationyear=2024

p1=Person("Gauss",25)
print(p1.name)
print(p1.age)
p2=Student("John",35)
print(p2.graduationyear)