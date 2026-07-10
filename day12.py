listt=[1,2,3,4,5,6,7,8]
print(listt)
for i in listt:
  print(i)
print(listt[1:5])
print(listt[1::2])
listt.append(9)
print(listt)
listt.insert(9,10)
print(listt)
listt.remove(10)
print(listt)
listt.pop(1)
print(listt)
listt.clear()
print(listt)

#tuple
tupple=(1,2,3,4,5,"rimel","tanjil")
print(tupple)
for i in tupple:
  print(i,end=" ")
print(tupple[1:3])

tupplee=(1,2,3)
c=tupple+tupplee
print(c)
print(tupplee*3)
t=list(tupple)
print(t)
a,b,c=tupplee
print(a,b,c)

dic={
    "name":"rimel",
    "age":23
}
print(dic)
print(dic["name"])
dic["mark"]=89
print(dic)
print(dic.get("mark"))
dic["name"]="tanjil ahmed"
print(dic)
dic.update({"name":"rimel","age":24})
print(dic)
del dic["name"]
print(dic)
dic.pop("age")
print(dic)
dic.popitem()
print(dic)
dic.clear()
print(dic)
dic["name"]="rimel"
dic["age"]=23
dic["mark"]=90
print(dic)
for key,value in dic.items():
  print(key,value)

for key in dic:
  print(key)

for value in dic.values():
  print(value)


dic.clear()
print(dic)

dic={
    "s1":{"name":"rimel","age":23,"mark":90},
    "s2":{"name":"tanjil","age":24,"mark":89}
}
print(dic)

print(dic["s1"]["name"])
dic["s1"]["name"]='rimel ahmed'
print(dic)
dic.update({"s1":{"name":"rimel",'age':25,"mark":99}})
print(dic)
for id,info in dic.items():
  print(id)
  for key,value in info.items():
    print(key,value)

del dic['s1']["name"]
print(dic)

dic.pop("s1")
print(dic)

dic.popitem()
print(dic)
dic.clear()
print(dic)

sett={1,2,3,4,5}
print(sett)
for i in sett:
  print(i)

sett.add(6)
print(sett)
sett.update({7,8,9,10})
print(sett)
sett.remove(10)
print(sett)
sett.discard(10)
print(sett)
sett.pop()
print(sett)
t=list(sett)
print(t)
f=set(t)
print(f)

from enum import unique
from enum import unique
from enum import unique
from re import search
fruits=["apple","mango","banana","jackfruits"]
print("apple" in fruits)
if "apple" in fruits:
  print("found")

for i in fruits:
  if i=="apple":
    print('found')
  else:
    print("not found")


num=[1,2,3,4,5,6,7]
for i in num:
  if i==3:
    print("found")
    break
  else:
    print("not found")

while True:
  search=input("enter your choice :").lower()
  if search=="end":
    break
  if search in fruits:
    print("found")
  else:
    print("not found")

count=0
for i in num:
  if i==3:
    count=count+1
print(count)

print(num.count(1))
unique=[]
for n in num:
  if not  unique:
    unique.append(n)
for i in unique:
  print(i,"appears",num.count(i))

dic={}
while True:
  key=input("enter your key :").lower()
  if key=="end":
    break
  value=input("enter your value :").lower()
  dic[key]=value
for k,v in dic.items():
  print(k,v)




import math
print(math.pi)
print(math.e)
print(math.pow(4,2))
print(math.sqrt(49))
print(math.factorial(5))
print(math.cos(60))



import random
print(random.random())
print(random.randint(1000,9999))
print(random.randrange(10,50,5))

name=["rimel","tanjil","rahim","ashik"]
print(random.choice(name))
print(random.sample(name,2))
otp=random.randint(1000,9999)
print("your otp is here :",otp)



class Student:
  def __init__ (self):
    self.name="rimel"
s=Student()
print(s.name)

class Car:
  def __init__ (self):
    self._name="rimel"

class Bike:
  def __init__ (self):
    self.__name="rimel"


from typing import Self
class Bank:
  def __init__ (self):
    self.__balance=500
  def get_balance(self):
    return self.__balance
  def set_balance(self,amount):
    if amount>=0:
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
class Bike(Car):
  def start(self):
    print("bike is not a car")
b=Bike()
b.start()


class Animal:
  def eat(self):
    print("animal can eat everything")
class Dog(Animal):
  def sound(self):
    print("dog can barking")

d=Dog()
d.eat()
d.sound()


class Animal:
  def barking(self):
    print("animal can barking")
class Dog:
  def barking(self):
    print("dog also can barking")
a=Animal()
a.barking()
d=Dog()
d.barking()


#lifo:last in first out
stack=[]
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)
stack.pop()
print(stack)



#queue
from collections import deque
queue=deque()
queue.append(10)
queue.append(20)
queue.popleft()
print(queue)


num=[2,4,6,7,3,9,2,10,14,11,12,13,5,4]

print(sorted(num))
print(num.sort())
print(num)



mark=[30,20,50,80,30,90,40]
mark.sort(reverse=True)
print(mark)

name=["rimel","tanjil",'rahim',"ashik","ekbal"]
name.sort()
print(name)

#linearsearch

arr=[1,2,3,4,5,6,7,8,9]
value=3
for i in arr:

  if i==value:
    print("found")
   

for i in range(len(arr)):
  if arr[i]==value:
    print("found",i)