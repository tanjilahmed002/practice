print("welcome to daily life tracker program")

name=input("nter your name :")
available_hour=float(input("enter your daily available hour :"))
daily_budget=float(input("enter your daily budget :"))


#daily activity 
study_python=float(input("enter your study python :"))
practice_python=float(input("enter your practice python :"))
other_activities=float(input("enter your oither activities :"))

total_activities=study_python+practice_python+other_activities


#expense 

food=float(input("enter your food expense :"))
transport=float(input("enter your transport expesne :"))
other=float(input("enter your other epense :"))

total_daily_expense=food+transport+other

remaining_budget=daily_budget-total_daily_expense
#time planning check

if total_activities>available_hour:
    print("you have planned more hours than available")
else:
    print("your daily plan is realistic")


#budget check

if total_daily_expense>daily_budget:
    print("you have exceded your daily budget")
else:
    print("you are within your daily budget ")


print("Name :",name)
print("Total planned hour :",total_activities)
print("Available :",total_daily_expense)
print("Remaining budget :",remaining_budget)

listt=[1,2,3,4,5,6,7]
print(listt)
for i in listt:
  print(i)

listt.append(8)
print(listt)

listt.insert(8,9)
print(listt)

print(listt[-6:-1])

listt.remove(9)
print(listt)
listt.pop()
print(listt)
listt.clear()
print(listt)

tupple=(1,2,3,4,5,6,7,"rimel")
print(tupple)
for i in tupple:
  print(i)

dic={"name":"rimel","age":23}
print(dic)
for key in dic:
  print(key)
for value in dic.values():
  print(value)
for key,value in dic.items():
  print(key,value)

dic["name"]="tanjil"
print(dic)

print(dic["name"])
print(dic.get("name"))
dic.update({"name":"rimel","age":21})
print(dic)

del dic["name"]
print(dic)
dic.pop("age")
print(dic)
dic.clear()
print(dic)

dic={
    "s1":{"name":"rimel","age":21},
    "s2":{"name":"tanjil","age":23}
}
print(dic)
for i,j in dic.items():
  print(i)
  for key,value in j.items():
    print(key,value)

dic.update({"s1":{"name":"rimel ahmed","age":24}})
print(dic)

dic.popitem()
print(dic)




from os import remove
sett={1,2,3,4,5,6,7}

print(sett)
for i in sett:
  print(i)

sett.add(8)
print(sett)
sett.update({9,10,11,12})
print(sett)
sett.remove(11)
print(sett)
sett.discard(11)
print(sett)
sett.pop()
print(sett)
sett.clear()
print(sett)

fruits=["mango","apple","banana"]
print("apple" in fruits)
if 'apple' in fruits:
  print("found")

num=[1,2,3,4,5,6,7]

for i in num:
  if i==2:
    print("found")
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

dic={}
while True:
  key=input("enter your key :")
  if key=="end":
    break
  value=input('enter your value :')
  dic[key]=value
for i,j in dic.items():
  print(i,j)


import math
print(math.pi)
print(math.e)
print(math.factorial(2))
print(math.cos(90))

import random
print(random.random())
print(random.randint(1000,9999))
print(random.randrange(100,999,1))
print(random.sample(fruits,2))
print(random.choice(fruits))

otp=random.randint(1000,9999)
print("your otp is here :",otp)

