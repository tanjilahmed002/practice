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
    