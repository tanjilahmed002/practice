listt=[1,2,3,4,5,6]
print(listt)

for i in listt:
  print(i)



print(listt[1::2])
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

tupple=(1,2,3,4,5)
print(tupple)

for i in tupple:
  print(i)

print(tupple[1:4])


dic={
    "name":"rimel",
    "age":23
}

print(dic)
for key in dic:
  print(key)
for value in dic.values():
  print(value)
print(dic['name'])
print(dic.get("age"))
dic["name"]="rimel ahmed"
print(dic)
dic.update({"name":"tanjil","age":24})
print(dic)
del dic["name"]
print(dic)
dic.pop("age")
print(dic)

dic={
    "s1":{"name":"rimel","age":23},
    's2':{"name":"tanjil","age":24}

}
print(dic)
print(dic["s1"]['name'])
dic["s3"]={"name":"rahim","age":25}
print(dic)
for id,info in dic.items():
  print(id)
  for key,value in info.items():
    print(key,":",value)

del dic["s1"]["name"]
print(dic)
dic.popitem()
print(dic)
dic.clear()
print(dic)

sett={1,2,5,7,8}
print(sett)
for i in sett:
  print(i)

sett.add(9)
print(sett)
sett.update({9,10,11,12,13})
print(sett)
sett.remove(13)
print(sett)
sett.discard(13)
print(sett)
sett.pop()
print(sett)
sett.clear()
print(sett)

#encapsalution

class Student:
  def __init__ (self):
    self.name="rimel"
s=Student()
print(s.name)

class Car:
  def __init__ (self):
    self._name="rimel"

class Car:
  def __init__ (self):
    self.__name="rimel"

from abc import ABC,abstractmethod
class Car(ABC):
  def start(self):
    pass
class Bike(Car):
  def start(self):
    print("car is not a bike")
b=Bike()
b.start()

class Car:
  def sound(self):
    print("this is not bike")
class Bike(Car):
  def start(self):
    print("bike is not car")
b=Bike()
b.sound()
b.start()

class Car:
  def sound(self):
    print("this is not bike")
class Bike(Car):
  def sound(self):
    print("bike is not car")
b=Bike()
c=Car()
c.sound()
b.sound()

