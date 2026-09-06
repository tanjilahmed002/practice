fruit=["banana","mango","apple"]
print("apple" in fruit)

if "apple" in fruit:
    print("found")
else:
    print("not found")


num=[1,2,3,4,5,6,7,8,9,1,2,1,1,2,3,4,5,4,1,2]
for i in num:
    if i==1:
        print("found")
    else:
        print("not found")


print(num.count(1))
print(fruit.index("apple"))

for i in range(len(num)):
    if num[i]==1:
        print("founad at :",i)


while True:
    search=input("enter your choice :").lower()
    if search=="end":
        break
    if search in fruit:
        print("found")
    else:
        print("not found")

unique=[]
for i in num:
    if not  unique:
        unique.append(i)
for j in unique:
    print(j,"appears at ",num.index(j))

count=0
for i in num:
    if i==1:
        count=count+1
print(count)

dic={}
while True:
    key=input("enter your key :")
    if key=="end":
        break
    value=input("enter your value :")
    dic[key]=value
for i,j in dic.items():
    print(i,j)

def function_name():
    print("hello")
function_name()

def function_name(name):
    print("hello",name)
function_name("rimel ahmed")

def function_name(a,b):
    return a+b
add=function_name(4,2)
print(add)
def function_name():
    return 100
print(function_name())

def info(name,age):
    print(name,age)
info(name="tanjil ahmed",age=23)

def single(x):
    return x*x
square=single(4)
print(square)

def mul(a,b):
    return a-b,a+b,a*b
x,y,z=mul(5,2)
print(x,y,z)


class Car:
    def __init__(self):
        self.name="rimel"
c=Car()
print(c.name)

class Car:
    def __init__(self):
        self._name="rimel"
class Car:
    def __init__(self):
        self.__name="rimel ahmed"

from abc import ABC,abstractmethod
class Bike(ABC):
    @abstractmethod
    def sound(self):
        pass
class Car(Bike):
    def sound(self):
        print("Car is not a bike")
v=Car()
v.sound()

class Bank:
    def __init__(self):
        self.__balance=500
    def get_balance(self):
        return self.__balance
    def set_balance(self,amount):
        if amount>0:
            self.__balance=amount
        else:
            print("invalid")
b=Bank()
print(b.get_balance())
b.set_balance(1000)
print(b.get_balance())

    