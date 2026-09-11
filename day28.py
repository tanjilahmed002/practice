listt=[1,2,3,4,5,6]
print(listt)

for i in listt:
    print(i)

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

tupple=(1,2,3,4,"rimel","tanjil")
print(tupple)

for i in tupple:
    print(i)

print(tupple[1:2])

dic={
    "name":"rimel",
    "age":23,
    "mark":60
}

print(dic)

print(dic["name"])

print(dic.get("age"))

dic["name"]="rimel ahmed"
print(dic["name"])

print(dic.update({"name":"rimel","age":24,"mark":77}))
print(dic)

del dic["age"]
print(dic)

dic.pop("name")
print(dic)
dic.popitem()
print(dic)

dic={
    "s1":{"name":"rimel","age":23},
    "s2":{"name":"tanjil","age":24}
}

print(dic)

for i,j in dic.items():
    print(i)
    for key,value in j.items():
        print(key,value)



print(dic["s1"]["name"])


dic["s1"]['name']="rimelk ahmed"

print(dic["s1"]["name"])


for key in dic:
    print(key)

for value in dic.values():
    print(value)

sett={1,2,3,4,5}
print(sett)

sett.add(6)
print(sett)

sett.update({7,8,9,10,11})
print(sett)

sett.remove(9)
print(sett)

sett.discard(10)
print(sett)

sett.pop()
print(sett)

sett.clear()
print(sett)


fruit=["apple","mango","banana"]
print("apple" in fruit)

if "apple" in fruit:
    print("found")
else:
    print("not found")

num=[1,2,3,4,5,6,7,1,2,1,1,3]
for i in num:
    if i==3:
        print("found")
    else:
        print("not found")

print(num.index(2)) 
print(num.count(3))

for i in range(len(num)):
    if num[i]==1:
        print(num[i],"appears at",i)

unique=[]
for i in num:
    if not unique:
        unique.append(i)
    for j in unique:
        print(i,"appears in",num.count(i))