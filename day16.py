class Bike:
    def __init__(self):
        self.name="rimel"
c=Bike()
print(c.name)

class Bike:
    def __init__(self):
        self._name="rimel"
class Bike:
    def __init__(self):
        self.__name="rimel"


from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def sound(self):
        pass
class Bike(Car):
    def sound(self):
        print("car is not a bike")
c=Bike()
c.sound()

class Dog:
    def eat(self):
        print("dog can eat everything")
class Cat(Dog):
    def sound(self):
        print("cat make sound meww")
d=Cat()
d.eat()
d.sound()




class Dog:
    def sound(self):
        print("dog can eat everything")
class Cat(Dog):
    def sound(self):
        print("cat make sound meww")
a=Cat()

a.sound()
e=Dog()
e.sound()




fruits=["apple","mango","banana"]
print("apple" in fruits)
if "apple" in fruits:
    print("found")
else:
    printa("not found")

num=[1,2,3,4,5,6]
for i in num:
    if i==3:
        print("found")
    else:
        print("not found")

count=0
for i in num:
    if i==3:
        count=count=1
print(count)

while True:
    search=input("enter your choice :").lower()
    if search=="end":
        break
    if search in fruits:
        print("found")
    else:
        print("not found")