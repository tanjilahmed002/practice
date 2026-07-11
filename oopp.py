class Car:
    def __init__ (self):
        self.name="rimel"
c=Car()
print(c.name)

class Car:
    def __intit__(self):
        self._name="rimel"
class Bike:
    def __init__ (self):
        self.__name="rimel"

class Bank:
    def __init__ (self):
        self.__balance=500
    def get_balance(self):
        return self.__balance
    def set_balance(self,amount):
        if amount>0:
            self.__balance=amount
        else:
            print("invalid balance")
    
b=Bank()
print(b.get_balance())
b.set_balance(1000)
print(b.get_balance())

from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("dog is a animal that can make a sound")
d=Dog()
d.sound()

class Cat:
    def eat(self):
        print("cat can eat all food")
class Dog(Cat):
    def soundd(self):
        print("dog can barking")
s=Dog()
s.eat()
s.soundd()

class Car:
    def start(self):
        print("car cannot drive iteslf")
class Bike:
    def handle(self):
        print("bike cannot handle itself")
c=Car()
c.start()
b=Bike()
b.handle()