listt=[1,2,3,4,5]
print(listt)
for i in listt:
    print(i)

listt.append(6)
print(listt)

listt.insert(5,7)
print(listt)

print(listt[1:3])

print(listt[-4:-1])

listt.remove(6)
print(listt)

listt.pop()
print(listt)

listt.clear()
print(listt)

tupple=(1,2,3,4,"rimel")
print(tupple)

for i in tupple:
    print(i)

print(tupple[1::2])

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



sett={1,2,3,4,5}
print(sett)

sett.add(7)
print(sett)

sett.update({6,8,9,11,12,10})
print(sett)

sett.remove(11)
print(sett)
sett.discard(11)
print(sett)
sett.pop()
print(sett)

sett.clear()
print(sett)


fruit=["apple","banana","mango"]
print(fruit)

for i in fruit:
    print(i)

print("apple" in fruit)


if "apple" in fruit:
    print("found")
else:
    print("not found")

num=[1,2,3,4,5,2,1,1,2,3,1]
for i in num:
    if i==1:
        print("found")
    else:
        print("not found")


print(num.count(1))

for i in range(len(num)):
    if num[i]==1:
        print(num[i],"appears at :",i)



unique=[]
for i in num:
    if not unique:
        unique.append(i)
    for j in unique:
        print(i,"appears in :",num.index(i))

dic={}
while True:
    key=input("enter your key :")
    if key=="end":
        break
    value=input("enter your value :")
    dic[key]=value
for key,value in dic.items():
    print(key,value)



while True:
    search=input("enter your fruit :").lower()
    if search=="end":
        break
    if search in fruit:
        print("found")
    else:
        print("not found")

dicc={
    "s1":{"name":"rimel ahmed","age":23},
    "s2":{'name':"taanjil ahmed","age":24}
}
print(dicc)

for i,j in dicc.items():
    print(i)
    for key,value in j.items():
        print(key,value)



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
        self.__name="rimel"

from abc import ABC,abstractmethod
class Carr(ABC):
    @abstractmethod
    def sound(self):
        pass
class Bike(Carr):
    def sound(self):
        print("car is not a bike")
b=Bike()
b.sound()

class Bike:
    def sound(self):
        print("this is bike")
class Motor(Bike):
    def eat(self):
        print("this is car")
n=Motor()
n.sound()
n.eat()

class Bike:
    def sound(self):
        print("this is bike")
class Motor:
    def sound(self):
        print("this is car")
n=Motor()
m=Bike()
m.sound()
n.sound()

def functionname():
    print("helo")
functionname()