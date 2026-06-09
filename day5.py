listt=[1,2,3,4,5,6,7,8]
print(listt)
for i in listt:
    print(i)

print(listt[2:6])
listt.append(9)
print(listt)
listt.insert(8,10)
print(listt)
listt.count(8)
print(listt)
listt.index(10)
print(listt)
listt.sort()
print(listt)
listt.remove(10)
print(listt)
listt.pop(8)
print(listt)
listt.clear()
print(listt)

#tuple 
tupple=("rimel","tanjil",1,2,3,4,5)
print(tupple)
for i in tupple:
    print(i)
print(tupple[1:3])

#dic

dic={
    "name":"rimel",
    "age":23
}
print(dic)
for key in dic:
    print(key)

for value in dic.values():
    print(value)

for key,value in dic.items():
    print(key,value)

print(dic["name"])
print(dic.get("name"))

dic["age"]=24
print(dic["age"])
dic.update({"name":"tanjil",'age':23})
print(dic)
del dic["name"]
print(dic)
dic.pop('age')
print(dic)
dic.clear()
print(dic)

dic={
    "s1":{"name":"rimel","age":23,"mark":90},
    "s2":{"name":"tanjil","age":24,"mark":99}
}
print(dic)
for id,info in dic.items():
    print(id)
    for key,value in info.items():
        print(key,value)

dic["s3"]={"name":"rahim",'age':25,"mark":89}
print(dic)

dic.popitem()
print(dic)
dic.clear()
print(dic)

#set
sett={1,2,3,4,5,6}
print(sett)
for i in sett:
    print(i)
sett.add(8)
print(sett)
sett.update({7,9,10,11,12})
print(sett)
sett.remove(12)
print(sett)
sett.discard(11)
print(sett)
sett.pop()
print(sett)
sett.clear()
print(sett)

fruits=["banana","mango",'apple']
print('apple' in fruits)
if "apple" in fruits:
  print("found")
else:
  print("not found")

num=[1,2,3,4,5,6,7,8]
for i in num:
  if i==3:
    print("found")
  else:
    print("not found")

while True:
  search=input("enter your choise type end for stop the loop :").lower()
  if search=="end":
    break
  if search in fruits:
    print("found")
  else:
    print("not found")

count=0
for i in num:
  if i==1:
    count=count+1
print(count)
dic={}
while True:
  key=input("enter your key and type end for stop the loop :")
  if key=="end":
    break
  value=input("enter your value :")
  dic[key]=value
for key,val in dic.items():
  print(key,val)


class Car:
    def __init__ (self):
        self.name="rimel"
c=Car()
print(c.name)

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
    def set__balance(self,amount):
        if amount>=0:
            self.__balance=amount
        else:
            print('invalid valance')
b=Bank()
b.get_balance()
print(b.get_balance())
b.set__balance(1000)
print(b.get_balance())

from abc import ABC,abstractmethod
class Animal(ABC):
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print('animal can make a sound')
d=Dog()
d.sound()

class Car:
    def start(self):
        print("car is car")
class Bike(Car):
    def sound(self):
        print("bike can sound")
c=Bike()
c.start()
c.sound()

class Car:
    def start(self):
        print("car is car")
class Bike(Car):
    def start(self):
        print("bike can sound")
f=Car()
c=Bike()
f.start()
c.start()

import math
print(math.pi)
print(math.e)
print(pow(2,3))
print(math.factorial(5))



import random
print(random.random())
print(random.randint(100,999))
print(random.randrange(100,999,10))
listt=[1,2,3,4,5,6,7]
print(random.choice(listt))   

print(random.sample(listt,2))

otp=random.randint(1000,9999)
print("your otp is here :",otp)