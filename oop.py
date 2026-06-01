# class Student:
#     def __init__(self):
#         self.name="rimel"
# s=Student()
# print(s.name)        

# class Student:
#     def __init__(self):
#         self.__name="rimel"

# class Bank:
#     def __init__(self):
#         self.__balance=5000
#     def get_balance(self):
#         return self.__balance
#     def set_balance(self,amount):
#         if amount>=0:
#             self.__balance=amount
#         else:
#             print("invalid balance")
# b=Bank()
# print(b.get_balance())
# b.set_balance(6000)
# print(b.get_balance())

# from abc import ABC,abstractmethod
# class Car(ABC):
#     @abstractmethod
#     def start(self):
#         pass
# class Tesla(Car):
#     def start(self):
#         print("tesla is starting")

# c=Tesla()

# print(c.start())

# class Student:
#     def __init__(self):
#         self.name="rimel"
# s=Student()
# print(s.name)

# class Student:
#     def __init__(self):
#         self._name="rimel"

# class Name:
#     def __init__(self):
#         self.__name="rimel"

# class Bank:
#     def __init__(self):
#         self.__balance=900
#     def get_balance(self):
#         return self.__balance
#     def set_balance(self,amount):
#         if amount>=0:
#             self.__balance=amount
#         else:
#             print("invalid")
# b=Bank()
# print(b.get_balance())
# b.set_balance(1000)
# print(b.get_balance())

# from abc import ABC,abstractmethod
# class Car(ABC):
#     @abstractmethod
#     def start(self):
#         pass
# class Tesla(Car):
#     def start(self):
#         print("tesla is starting")

# n=Tesla()
# print(n.start())

class Animal:
    def cat(self):
        print("cat can sound meow")
    
class Dog:
    def cat(self):
        print("dog is barking")

c=Dog()
d=Animal()
c.cat()
d.cat()



class Student:
  def __init__(self):
    self.name="rimel"
s=Student()
print(s.name)


class Student:
  def __init__ (self):
    self._name="rimel"

class Student:
  def __init__(self):
    self.__name__="rinel"

class Bank:
  def __init__(self):
    self.__name="rimel"
  def get_name(self):
    return self.__name
  def set_name(self,value):
    self.__name=value
n=Bank()
#n.get_name()
print(n.get_name())
n.set_name("tanjil")
print(n.get_name())

from abc import ABC,abstractmethod
class Car(ABC):
  def start(self):
    pass
class Bike(Car):
  def start(self):
    print("bike is not a part of a car")
c=Bike()
c.start()

class Car:
  def start(self):
    print("this is a car")
class Bike(Car):
  def sound(self):
    print("bike can sound")
b=Bike()
b.start()
b.sound()

class Car:
  def sound(self):
    print("this is a car")
class Bike(Car):
  def sound(self):
    print("bike can sound")
b=Bike()
c=Car()
c.sound()
b.sound()

from logging import log
import math
print(math.pi)
print(math.e)
print(math.pow(2,4))
print(math.factorial(5))
print(math.log(10))
print(math.cos(12))


import random
print(random.Random)
print(random.randint(100,999))
print(random.randrange(1000,9999,10))
listt=[1,2,3,4,5,6,7,8,9,10]
print(random.choice(listt))
print(random.sample(listt,3))

otp=random.randint(1000,9999)
print("your otp is :",otp)

fruits=["banana","mango","apple","jackfruit"]
print("apple" in fruits)

if "apple" in fruits:
  print("found")
else:
  print("not found")

num=[1,2,3,4,5,6,7,8,9]
for i in num:
  if i==3:
    print("found")
  else:
    print("not found")

while True:
  search=input("enter your choice & type end for stop the loop :").lower()
  if search=="end":
    break
  if search in fruits:
    print("found")
  else:
    print("not found")


empty={}
while True:
  key=input("enter your key & type end for stop :")
  if key=="end":
    break
  value=input("enter your value :")
  empty[key]=value
print(empty)


num=[1,2,3,3,3,3,4,5,6,7,8,9]
count=0
for i in num:
  if i==3:
    count=count+1
print(count)


listt=[1,2,3,4,5,6,7,8,9]
print(listt)

for i in listt:
  print(i,end=" ")

listt.append(10)
print(listt)

listt.insert(10,11)
print(listt)

listt.extend(num)
print(listt)

listt.sort()
print(listt)

from os import remove
listt.remove(11)
print(listt)

listt.pop(0)
print(listt)

listt.clear()
print(listt)

sett=(1,2,3,4,5,6,7,8,9)
print(sett)

for i in sett:
  print(i,end=" ")

print(sett[0:3])

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

dic["name"]="rimel ahmed"
print(dic["name"])

dic.update({"name":"rimel","age":24})
print(dic)

del dic["name"]
print(dic)

dic.pop("age")
print(dic)

dic={
    "s1":{"name":"rimel","age":23},
    "s2":{"name":"tanjil","age":24}
}
print(dic)

dic["s3"]={"name":"rahim","age":25}
print(dic)

for id,info in dic.items():
  print(id)
  for key,value in info.items():
    print(key,value)

sett={1,2,3,4,5,6,7,8,9}
print(sett)

for i in sett:
  print(i)

sett.add(10)
print(sett)

sett.update({11,12,13})
print(sett)

from os import remove
sett.remove(13)
print(sett)

sett.discard(12)
print(sett)

sett.pop()
print(sett)

sett.clear()
print(sett)




