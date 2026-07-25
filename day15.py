listt=[1,2,3,4,5,6]
print(listt)
for i in listt:
  print(i)
listt.append(7)
print(listt)
listt.insert(7,8)
print(listt)
print(listt[-6:-1])
listt.remove(7)
print(listt)
listt.pop(6)
print(listt)
listt.clear()
print(listt)

tupple=(1,2,3,4,"rimel")
print(tupple)
for i in tupple:
  print(i)
t=list(tupple)
print(t)
l=tuple(t)
print(l)


dic={
    "name":"rimel",
    "age":23
}
print(dic)
for key,value in dic.items():
  print(key,value)
for key in dic:
  print(key)
for value in dic.values():
  print(value)
print(dic["name"])
print(dic.get("age"))
dic["name"]="rimel ahmed"
print(dic["name"])
dic.update({"name":"rimel","age":23})
print(dic)
del dic["name"]
print(dic)
dic.pop("age")
print(dic)
dic.clear()
print(dic)

dic={
    "s1":{"name":"rimel","age":23},
    "s2":{"name":"rimel","age":24}
}
print(dic)
print(dic["s1"]["name"])
dic["s1"]["name"]="rimel ahmed"
print(dic["s1"]["name"])

dic.update({"s1":{"name":"rimel","age":25}})
print(dic)

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
sett.update({8,9,10,11,12,13,13})
print(sett)
sett.remove(13)
print(sett)
sett.discard(13)
print(sett)
sett.pop()
print(sett)
sett.clear()
print(sett)


fruit={"apple","mango","banana"}
print("apple" in fruit)
if "apple" in fruit:
  print("found")

num=[1,2,3,4,5]
for i in num:
  if i==3:
    print("found")
  else:
    print("not found")

count=0
for i in num:
  if i==2:
    count=count+1
print(count)
while True:
  search=input('enter your choice :').lower()
  if search=="end":
    break
  if search in fruit:
    print("found")
  else:
    print("not found")
dic={}
while True:
  key=input("enter your key :")
  if key=="end":
    break
  value=input("enter your value :")
  dic[key]=value
for i,k in dic.items():
  print(i,k)