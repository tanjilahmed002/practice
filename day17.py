listt=[1,2,3,4,5,6]
print(listt)
for i in listt:
    print(i)

print(listt[2:4])
print(listt[-4:-2])
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

tupple=(1,2,3,4,5,6)
print(tupple)
for i in tupple:
    print(i)

print(tupple[2::2])

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

print(dic["age"])

print(dic.get("name"))

dic["age"]=24
print(dic)

dic.update({"name":"rimel ahmed","age":23})
print(dic)

del dic['name']
print(dic)
dic.pop("age")
print(dic)
dic.clear()
print(dic)

dic={
    "s1":{"name":"rimel","age":24},
    "s2":{"name":"tanjil","age":23}
}
print(dic)
for i,j in dic.items():
    print(i)
    for key,value in j.items():
        print(key,value)

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
sett.update({7,8,9,10,11})
print(sett)

sett.remove(11)
print(sett)
sett.discard(11)
print(sett)
sett.pop()
print(sett)
sett.clear()
print(sett)