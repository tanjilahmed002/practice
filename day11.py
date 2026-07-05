mark=80
if mark>=50:
    print("pass")
else:
    print("fail")


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
print(random.random())
print(random.randint(1000,9999))
print(random.randrange(100,999,2))




fruits=["apple","mango","banana"]
print("apple" in fruits)
if "apple" in fruits:
    print("found")
else:
    print("not found")



num=[1,2,3,4,5]

for i in num:
    if i==3:
        print("found")
    else:
        print("not found")


while True:
    seach=input("enter your fruits :")
    if seach=="end":
        break
    if seach in fruits:
        print("found")
    else:
        print("not found")

count=0
for i in num:
    if i==2:
        count=count+1
print(count)


nn=[1,2,3,4,5,6]
print(nn)
for i in nn:
    print(i)

nn.append(7)
print(nn)
nn.insert(7,8)
print(nn)


sett=(1,2,3,4,5,6)
print(sett)
for i in sett:
    print(i)

dicc={
    "name":"rimel",
    "age":23
}
print(dicc)

for key,value in dicc.items():
    print(key,value)

for key in dicc:
    print(key)

for value in dicc.values():
    print(value)

print(dicc['age'])

print(dicc.get("name"))
dicc["name"]="tanjil"
print(dicc)

dicc.update({"name":"tanjil ahmed","age":24})
print(dicc)