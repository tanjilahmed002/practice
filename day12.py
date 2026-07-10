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