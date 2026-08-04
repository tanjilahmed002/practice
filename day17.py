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