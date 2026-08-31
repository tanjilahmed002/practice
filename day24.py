def function_name():
    print("hello")
function_name()


def function_name(name):
    print("hello",name)
function_name("rimel")


def function_name(a,b):
    return a+b
add=function_name(4,2)
print(add)

def sq():
    return 200
sq()

def info(name,age):
    print(name,age)
info(name="rimel ahmed",age=23)

def square(x):
    return x*x
ss=square(6)
print(ss)

def mul(a,b):
    return a+b,a-b,a*b
x,y,z=mul(6,4)
print(x,y,z)


class Name:
    def __init__(self):
        self.name="rimel"
c=Name()
print(c.name)


class Bike:
    def __init__(self):
        self._name="rimel"
class Car:
    def __init__(self):
        self.__name="rimel"


from abc import ABC,abstractmethod
class Bike(ABC):
    @abstractmethod
    def sound(self):
        pass
class Car(Bike):
    def sound(self):
        print("car is not a bike")
b=Car()
b.sound()