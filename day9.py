listt=[1,2,3,4,5,6]
print(listt)
for i in listt:
  print(i)

listt.append(7)
print(listt)
listt.insert(7,8)
print(listt)
listt.remove(8)
print(listt)
listt.pop(6)
print(listt)
listt.clear()
print(listt)

tupple=(1,2,3,4,5,"rimel","tanjil")
print(tupple)
for i in tupple:
  print(i)
print(tupple[2:4])

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
print(dic['age'])
print(dic.get("name"))
dic["age"]=24
print(dic)
dic.update({"name":"tanjil","age":23})
print(dic)
del dic["age"]
print(dic)
dic.pop("name")
print(dic)
dic.clear()
print(dic)


dic={
    "s1":{"name":"rimel","age":23},
    "s2":{"name":"tanjil","age":24}

}
print(dic)

for id,info in dic.items():
  print(id)
  for key,value in info.items():
    print(key,value)
dic["s3"]={"name":"rahim","age":25}
print(dic)
print(dic["s1"]["name"])
dic.popitem()
print(dic)
dic.clear()
print(dic)

sett={1,2,3,4,5,6}
print(sett)
for i in sett:
  print(i)
sett.add(7)
print(sett)
sett.update({8,9})
print(sett)
settt={10,11,12,13}
result=sett.union(settt)
print(result)
rr=sett.intersection(settt)
print(rr)
print(sett)
sett.remove(9)
print(sett)
sett.discard(9)
print(sett)
sett.pop()
print(sett)
sett.clear()
print(sett)

fruits={"mango","apple","banana"}
print("apple" in fruits)
if "apple" in fruits:
  print("found")
else:
  print("not found")

num=[1,2,3,4,5,6]
for i in num:
  if i==3:
    print("found")
  else:
    print("not found")

while True:
  search=input("enter choice fruit and type end for stop the loop :").lower()
  if search=="end":
    break
    
  if search==fruits:
    print("found")
  else:
    print("not found")

count=0
for i in num:
  if i==2:
    count=count+1
print(count)

dic={}
while True:
  key=input("enter your key :").lower()
  if key=="end":
    break
  value=input("enter your value :").lower()
  dic[key]=value
for key,value in dic.items():
  print(key,value)

  import math
print(math.pi)
print(math.e)
print(math.factorial(4))
import random
print(random.random())
print(random.randint(100,999))
print(random.randrange(1000,9999,10))
listt=[1,2,3,4,5,"rimel",'tanjil']
print(random.choice(listt))
print(random.sample(listt,2))


otp=random.randint(1000,9999)
print("your otp is here :",otp)


class Car:
  def __init__ (self):
    self.name="rimel"
c=Car()
print(c.name)
class Bike:
  def __init__ (self):
    self._name="rimel"

class Bike:
  def __init__ (self):
    self.__name="rimel"


from abc import abstractmethod
from abc import ABC,abstractmethod
class Car(ABC):
  @abstractmethod
  def name(self):
    pass
class Bike(Car):
  def name(self):
    print("this is not a car ")
b=Bike()
b.name()


class Animal:
  def sound(self):
    print("animal can sound")
class Dog(Animal):
  def eat(self):
    print("dog can eat food")
d=Dog()
d.sound()
d.eat()

class Animal:
  def eat(self):
    print("animal can sound")
class Dog(Animal):
  def eat(self):
    print("dog can eat food")
a=Animal()

d=Dog()
a.eat()
d.eat()