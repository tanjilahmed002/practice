import random
print(random.random())

print(random.randint(1000,9999))
print(random.randrange(100,999,10))

fruit=["apple","mango","banana",1,2,3,4,5,6,7]
print(random.sample(fruit,2))
print(random.choice(fruit))

otp=random.randint(1000,9999)
print("here is your otp :",otp)


import math
print(math.e)
print(math.pi)
print(math.factorial(3))


class Cat:
    def __init__(self):
        self.name="rimel"
c=Cat()
print(c.name)
class Cat:
    def __init__(self):
        self._name="rimel"
class Cat:
    def __init__(self):
        self.__name="rimel"

from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def sound(self):
        pass
class Bike(Car):
    def sound(self):
        print("this is not car")
a=Bike()
a.sound()