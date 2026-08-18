def function_name():
    print("hello")
function_name()

def function_name(name):
    print("hello",name)
function_name("rimel ahmed")

def function_name(a,b):
    return a+b
add=function_name(2,4)
print(add)

def function_name():
    return 100
print(function_name())

def student(name,age):
    print(name,age)
student(name="rimel ahmed",age=23)

def single(x):
    return x*x
madd=single(34)
print(madd)

def mul(a,b):
    return a+b,a-b,a/b,a*b
w,x,y,z=mul(5,3)
print(w,x,y,z)

def function_name():
  print("hello")
function_name()

def function_name(name):
    print("hello",name)
function_name("rimel")

def add(a,b):
    return a+b
sum=add(3,4)
print(sum)

def add():
    return 100

print(add())



def function_name(name,age):
    print(name,age)
function_name(name="rimel",age=23)


def square(x):
    return x*x
addd=square(3)
print(addd)

def mull(a,b):
    return a+b,a-b
x,y=mull(6,3)
print(x,y)

class Car:
    def __init__ (self):
        self.name="rimel"
c=Car()
print(c.name)
class Bike:
    def __init__(self):
        self._name="tanjil"


class Honda:
    def __int__(self):
        self.__name="rimel ahmed"


from abc import ABC,abstractmethod
class Bike(ABC):
    @abstractmethod
    def sound(self):
        pass
class Kook(Bike):
    def sound(self):
        print("this is not a car")
k=Kook()
k.sound()


class Bike:
    def sss(self):
        print("is a cow")
class Cook(Bike):
    def dd(self):
        print("is not a coq")
b=Bike()
b.sss()
d=Cook()
d.dd()