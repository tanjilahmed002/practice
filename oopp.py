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
        self._name="rimel"

class Girl:
    def __init__ (self):
        self.__name="tanjil"



from abc import ABC,abstractmethod
class Doogy(ABC):
    def sound(self):
        pass
class Cat(Doogy):
    def sound(self):
        print("cat is not a doog")
c=Cat()

c.sound()

class Name:
    def name(self):
        print("my name is rimel")
class Age(Name):
    def age(self):
        print("i am 21 years old")
a=Age()
a.name()
a.age()

class Cook:
    def rice(self):
        print("i cannot cook everything")
class Eat:
    def eat(self):
        print("i can eat everything")
c=Cook()
c.rice()
e=Eat()
e.eat()



class Bank:
    def __init__(self):
        self._balance=500
    def get_balance(self):
        return self._balance
    def set_balance(self,amount):
        if amount>0:
            self._balance=amount
        else:
            print("invalid balance")

b=Bank()
print(b.get_balance())
b.set_balance(1000)
print(b.get_balance())


class Gopod:
    def __init__ (self):
        self.name="rimel"
g=Gopod()
print(g.name)


class DOOg:
    def __init__ (self):
        self._namee="rimel"

from abc import ABC,abstractmethod
class King(ABC):
    @abstractmethod
    def sounf(self):
        pass
class Queen(King):
    def sounf(self):
        print("you are queen only king of my heart")

q=Queen()
q.sounf()

class Bank:
    def balance(self):
        print("yopur account is empty")
class Person(Bank):
    def amount(self):
        print("your amount is not big")
p=Person()
p.balance()
p.amount()

class Cat:
    def sound(self):
        print("cat can sound meww")
class Dog:
    def soundd(self):
        print("dog can barking")
c=Cat()
c.sound()
d=Dog()
d.soundd()




fruits=["apple","mango","banana"]
print(fruits)
if 'apple' in fruits:
    print("found")
else:
    print("not found")

num=[1,2,3,4,5,6,7]
for i in num:
    if i==3:
        print("found")
    else:
        print("not found")

count=0
for i in num:
    if i==3:
        count=count+1
print(count)

while True:
    search=input("enter your choice :")
    if search=="end":
        break
    if search in fruits:
        print("found")
    else:
        print("not found")

dic={}
while True:
    key=input('enter your key :')
    if key=="end":
        break
    value=input("enter your value :")

    dic[key]=value

print(dic)

listt=[1,2,3,4,5,6,7]
print(listt)