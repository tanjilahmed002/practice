print("welcome to result system")

#encalpsulation

class Student:
    def __init__(self):
        self.name="rimel"
s=Student()
print(s.name)

class Student:
    def __init__(self):
        self._name="rimel"

class Student:
    def __init__(self):
        self.__name="name"


#abstraction

from abc import ABC,abstractmethod
class Car(ABC):
    def start(self):
        pass
class Bike(Car):
    def start(self):
        print("bike is not a car")

b=Bike()
b.start()

#inheritance

class Animal():
    def eat(self):
        print("animal can eat everything")
class Dog(Animal):
    def bark(self):
        print("dog can bark and eat everything")
d=Dog()
d.eat()
d.bark()

#polymorshim

class Animal():
    def eat(self):
        print("animal can eat everything")
class Dog(Animal):
    def eat(self):
        print("dog can bark and eat everything")
a=Animal()
d=Dog()


a.eat()
d.eat()
