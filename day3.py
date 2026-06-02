#encapsulation
class Student:
    def __init__(self):
        self.name="rimel ahmed"
c=Student()
print(c.name)

class Student:
    def __init__(self):
        self._name="rimel"

class Student:
    def __init__(self):
        self.__name="rimel"

class Bank:
    def __init__(self):
        self.__name="rimel ahmed"
    def get_name(self):
        return self.__name
    def set_name(self,amount):
        
        self.__name=amount
b=Bank()
print(b.get_name())
b.set_name(500)
print(b.get_name())
        

#abstractmethod

from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def start(self):
        pass
class Bike(Car):
    def start(self):
        print("bike is not part of a car")
c=Bike()
c.start()

#inheritance

class Car:
    def start(self):
        print("this is start from here")

class Bike(Car):
    def sound(self):
        print("bike can sound")
x=Bike()
x.start()
x.sound()


#polymorphism

class Car:
    def start(self):
        print("this is start from here")

class Bike(Car):
    def sound(self):
        print("bike can sound")
x=Bike()
y=Car()
y.start()
x.sound()