def myname():
  print("rimel ahmed ")
myname()


def myname(name):
  print(name)
myname("rimel")

def add(a,b):
  return a+b
l=add(3,2)
print(l)

def info():
  return 100
print(info())

def info(name,age):
  print(name,age)
info(name="rimel",age=23)


def total(*number):
  print(number)
total(1,2,3,4,5)

def total(**info):
  print(info)
total(name="rimel",age=23)

def total(a,b,*arg,**war):
  print(a,b)
  print(arg)
  print(war)
total(1,2,3,4,x=100,y=200)

def square(x):
  return x*x
s=square(5)
print(s)

def cal(a,b):
  return a+b,a-b
x,y=cal(3,4)
print(x,y)

def info():
  x=10
  print(x)
info()

x=100
def info():
  print(x)
info()

x=1200
def info():
  global x
  x=120
  print(x)
info()


def outer():
  x=100
  def inner():
    nonlocal x
    x=120
    
    print(x)
  inner()
outer()

import math
print(math.pi)
print(math.ceil)
print(math.e)
print(math.pow(2,3))
print(math.sqrt(25))
print(math.factorial(49))
print(math.cos(10))
print(math.log(100))


import random
print(random.random())
random.randint(1000,9999)
random.randrange(1000,9999,10)

ll=["rimel","tanjil","rahim","hasan"]
print(random.choice(ll))

tt=[1,2,3,4,5,6]
random.sample(tt,3)

otp=random.randint(1000,9999)
print("otp is :",otp)


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
    self.__name="rimel"



class Bank:
  def __init__(self):
    self.__balance=500
  def get_balance(self):
    return self.__balance
  def set_balance(self,amount):
    if amount >=0:
      self.__balance=amount
    else:
      print("invalid balance")
b=Bank()
print(b.get_balance())
b.set_balance(1000)
print(b.get_balance())


from abc import ABC,abstractmethod
class Car(ABC):
  @abstractmethod
  def start(self):
    pass
class Tesla(Car):
  def start(self):
    print("tesla is a car")
c=Tesla()
c.start


class Animal:
  def eat(self):
    print("animal can eat food")
class Cat(Animal):
  def food(self):
    print("cat can eat fish")

c=Cat()
c.eat()
c.food()

class Animal:
  def eat(self):
    print("animal can eat food")
class Cat(Animal):
  def eat(self):
    print("cat can eat fish")

c=Cat()
a=Animal()
a.eat()

c.eat()
