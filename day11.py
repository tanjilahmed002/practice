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