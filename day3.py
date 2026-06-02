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

#math
import math
print(math.pi)
print(math.e)
print(math.log(10))
print(math.factorial(5))
print(math.sin(20))

#random

import random

print(random.random())
print(random.randint(100,999))
print(random.randrange(100,999,10))

listt=[1,2,3,4,5,6,7,8,9,"rimel","tanjil"]
print(random.choice(listt))

print(random.sample(listt,3))

#otp generator

otp=random.randint(1000,9999)
print("your otp is here :",otp)

#list in search
fruits=["apple","mango","banana"]
print("apple" in fruits)
if 'apple' in fruits:
    print("found")
else:
    print("not found")

num=[1,2,3,4,5,6,7,8,9,10]
for i in num:
    if i==3:
        print("found")
    else:
        print("not found")


while True:
    search=input("enter your choice & type end :").lower()
    if search=="end":
        break
    if search in fruits:
        print("found")
    else:
        print("not found")



#frequency counter

count=0
for i in num:
    if i==2:
        count+=1
print(count)

dic={}
while True:
    key=input("enter your key & type end for stop the loop :").lower()
    if key=="end":
        break
    value=input("enter your value :")
    dic[key]=value
for key,value in dic.items():
    print(key,":",value)


#list in python
listtt=[1,2,3,4,5,6,7,8,9]
print(listtt)
for i in listtt:
    print(i,end=" ")


listtt.append(10)
print(listtt)
listtt.insert(10,11)
print(listtt)

listtt.remove(11)
print(listtt)
listtt.pop(0)
print(listtt)
listtt.clear()
print(listtt)

#tuple in python

tupple=(1,2,3,4,5,6,7,8)
print(tupple)
 
for i in tupple:
    print(i)

print(tupple[0:3])


#dictionary in python

dicc={
    "name":"rimel",
    "age":23
}
for key in dicc:
    print(dicc)

for value in dicc.values():
    print(value)

for key,value in dicc.items():
    print(key,":",value)

print(dicc["age"])
print(dicc.get("name"))
dicc["age"]=24
print(dicc)
dicc.update({"name":"rimel ahmed","age":25})
print(dicc)
del dicc["age"]
print(dicc)
dicc.pop("name")
print(dicc)
dicc={
    "s1":{"name":"rimel","age":23},
    "s2":{"name":"tanjil","age":24}
}
dicc["s3"]={"name":"rahim","age":25}
print(dicc)
for id,info in dicc.items():
    print(id)
    for key,value in info.items():
        print(key,value)


#set in python

sett={1,2,3,4,5,6,7}
print(sett)
for i in sett:
    print(i)

sett.add(8)
print(sett)
sett.update({9,10,11,12,14,13})
print(sett)

sett.remove(1)
print(sett)
sett.discard(1)
print(sett)
sett.pop()
print(sett)
sett.clear()
print(sett)