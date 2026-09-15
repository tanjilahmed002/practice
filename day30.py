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