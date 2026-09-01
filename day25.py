class Car:
    def __init__(self):
        self.name="rimel"
c=Car()
print(c.name)


class Bike:
    def __init__(self):
        self._name="rimel"

class Bike:
    def __init__(self):
        self.__name="rimel ahmed"


from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def sound(self):
        pass
class Bike(Car):
    def sound(self):
        print("bike is not a car")
b=Bike()
b.sound()

class Animal:
    def sound(self):
        print("animal can sound ")

class Dog(Animal):
    def eat(self):
        print("dog is a animal")
d=Dog()
d.sound()
d.eat()
