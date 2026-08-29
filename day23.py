listt=[1,2,3,4,5,6,7]
print(listt)

for i in listt:
    print(i)

listt.append(8)
print(listt)
listt.insert(8,9)
print(listt)

print(listt[-3:-1])

tupple=(1,2,3,4,"rimel","tanjil")
print(tupple)

for j in tupple:
    print(j)


dic={
    "name":"rimel",
    "age":23
}
print(dic)
print(dic["age"])

dic["name"]="rimel ahmed"
print(dic)

listt.remove(7)
print(listt)
listt.pop(7)
print(listt)
listt.clear()
print(listt)

print(dic.get("name"))

dic.update({"name":"rimel","age":24})
print(dic)

for key in dic:
    print(key)

for value in dic.values():
    print(value)

for key,value in dic.items():
    print(key,value)


del dic["age"]
print(dic)

dic.pop("name")
print(dic)

dic["name"]="tanjil ahmed"
print(dic)
dic.pop("name")
print(dic)

dic.update({"name":"tanjil","age":23})
print(dic)
dic.popitem()
print(dic)

dic.clear()
print(dic)

dic={
    "s1":{"name":"rimel","age":23},
    "s2":{"name":"tanjil","age":24}
}
print(dic)

print(dic["s1"]["name"])

dic["s1"]["name"]="rimel ahmed"
print(dic["s1"]["name"])

dic.update({"s1":{"name":"rimel","age":25}})
print(dic)

dic.popitem()
print(dic)
del dic["s1"]
print(dic)

sett={1,2,3,4,5}
sett.add(6)
print(sett)

sett.update({7,8,9,10,11,12,13})
print(sett)

sett.remove(11)
print(sett)
sett.discard(11)
print(sett)

sett.pop()
print(sett)

sett.clear()
print(sett)

fruits=["rimel",'apple',"banana","mango"]
print('apple' in fruits)
if "apple" in fruits:
    print("found")
else:
    print("not found")


num=[1,2,3,4,5]
for i in num:
    if i==2:
        print("found")
    else:
        print("not found")


while True:
    search=input("enter your choice & type end for stop this loop :").lower()
    if search=="end":
        break
    if search in fruits:
        print("found")
    else:
        print("not found")


counnt=0
for i in num:
    if i==1:
        counnt=counnt+1
print(counnt)

dic={}
while True:
    key=input("enter your key :")
    if key=="end":
        break
    value=input("enter your value :")
    dic[key]=value
for key,value in dic.items():
    print(key,value)

import random
print(random.randint(1000,9999))
print(random.random())
print(random.randrange(100,999,10))
print(random.choice(fruits))
print(random.sample(fruits,2))

otp=random.randint(1000,9999)
print("your otp is here :",otp)


class Car:
    def __init__(self):
        self.name="rimel ahmed"
c=Car()
print(c.name)

class Name:
    def __init__(self):
        self._na="rimel"

class Bike:
    def __init__(self):
        self.__nam="rimel ahmed"


class Bank:
  def __init__(self):
    self.__balance=500
  def get_balance(self):
    return self.__balance
  def set_balance(self,amount):
    if amount>0:
      self.__balance=amount
    else:
      print("invalid amount")

b=Bank()
print(b.get_balance())
b.set_balance(100)
print(b.get_balance())