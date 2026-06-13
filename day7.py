listt=[1,2,3,4,5]
print(listt)
for i in listt:
  print(i)
listt.append(7)
print(listt)
listt.insert(6,6)
print(listt)
listt.remove(6)
print(listt)
listt.pop(5)
print(listt)
listt.clear()
print(listt)

tupple=(1,2,3,4)
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

del dic["name"]
print(dic)
sett={1,2,3,4,5}
print(sett)
for i in sett:
  print(i)

sett.add(6)
print(sett)
sett.update({7,8,9})
print(sett)


fruits=["apple","mango","banana"]
print("apple" in fruits)
if "apple" in fruits:
  print('found')
else:
  print("found")

num=[1,2,3,4,5,6,7]
for i in num:
  if i==3:
    print("found")
  else:
    print("not found")

while True:
  search=input("enter your fruits :").lower()
  if search=="end":
    break
  if search in fruits:
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
  key=input("enter your key :")
  if key=="end":
    break
  value=input("enter your value :")
  dic[key]=value
for key,value in dic.items():
  print(key,value)

import math

print(math.pi)
print(math.e)
print(math.factorial(5))

import random
random.random()
print(random.randint(100,999))
print(random.randrange(100,999,10))
listt=["rimel","tanjil","rahim",1,2,3,4,5]

print(random.choice(listt))
print(random.sample(listt,2))

otp=random.randint(1000,9999)
print("your otp is here :",otp)