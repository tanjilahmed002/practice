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