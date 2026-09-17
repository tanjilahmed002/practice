listt=[1,2,3,4,5]
print(listt)
for i in listt:
    print(i)

listt.append(6)
print(listt)

listt.insert(5,7)
print(listt)

print(listt[1:3])

print(listt[-4:-1])

listt.remove(6)
print(listt)

listt.pop()
print(listt)

listt.clear()
print(listt)

tupple=(1,2,3,4,"rimel")
print(tupple)

for i in tupple:
    print(i)

print(tupple[1::2])

dic={
    "name":"rimel",
    "age":23
}
print(dic)

for key in dic:
    print(key)

for value in dic.values():
    print(value)

for key,value in dic.items():
    print(key,value)



sett={1,2,3,4,5}
print(sett)

sett.add(7)
print(sett)

sett.update({6,8,9,11,12,10})
print(sett)

sett.remove(11)
print(sett)
sett.discard(11)
print(sett)
sett.pop()
print(sett)

sett.clear()
print(sett)


fruit=["apple","banana","mango"]
print(fruit)

for i in fruit:
    print(i)

print("apple" in fruit)
