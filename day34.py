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



del dicc["age"]
print(dicc)

dicc.pop("name")
print(dicc)


dicc={
    "s1":{"name":"rimel","age":23},
    "s2":{"name":"tanjil","age":24}
}
print(dicc)

for i,j in dicc.items():
    print(i)
    for key,value in j.items():
        print(key,value)



print(dicc["s1"]["name"])


del dicc["s2"]["name"]
print(dicc)

dicc.pop("s2")
print(dicc)

dicc.popitem()
print(dicc)
sett={1,2,3,4,5}
print(sett)

for i in sett:
    print(i)

sett.add(6)
print(sett)
sett.update({7,8,9,10})
print(sett)

sett.remove(8)
print(sett)

sett.discard(8)
print(sett)
sett.pop()
print(sett)

sett.clear()
print(sett)


fruit=["apple","mango","banana"]
print(fruit)

print("apple" in fruit)

if "apple" in fruit:
    print("found")
else:
    print("not found")


num=[1,2,3,4,5,6,7,1,2,3,3,3]
for i in num:
    if i==3:
        print("found")
    else:
        print("not found")

while True:
    search=input("enter your choice :").lower()
    if search=="end":
        break
    if search in fruit:
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
    value=input("enter your value :")
    dic[key]=value
for i,j in dic.items():
    print(i,j)

print(num.count(3))
for i in range(len(num)):
    if num[i]==3:
        print(num[i],"appears in :",i)