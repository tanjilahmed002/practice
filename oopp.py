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

listt=[1,2,3,43,66,57,34,88,35,67,23,22]
print(sorted(listt))
listt.sort(reverse=True)
print(listt)
name=["rimel","tanjil","rahim","fahim","ashik","ekbal","roman"]
name.sort()
print(name)

stack=[]
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
print(stack)
stack.pop()
print(stack)

from collections import deque
queue=deque()
queue.append(10)
queue.append(20)
queue.append(30)
queue.popleft()
print(queue)




class Bike:
    def __init__ (self):
        self.name="rimel"
e=Bike()
print(e.name)


class Book:
    def __init__ (self):
        self._name+"rimel"

class Girl:
    def __init__ (self):
        self.__name="tanjil"