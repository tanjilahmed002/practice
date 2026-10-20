print("hello world")

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



listt.pop()
print(listt)

listt.clear()
print(listt)


tupple=(1,2,3,4,5,"rimel","tanjil")
print(tupple)

for k in tupple:
    print(k)

print(tupple[0::2])

dicc={
    "name":"rimel ahmed",
    "age":23
}
print(dicc)

for key,value in dicc.items():
    print(key,value)

for ley in dicc:
    print(ley)


for value in dicc.values():
    print(value)

print(dicc["age"])


print(dicc.get("name"))

dicc["name"]="tanjil ahmed"
print(dicc)

dicc.update({"name":"rimel","age":25})
print(dicc)
