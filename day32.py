sett={1,2,3}
print(sett)

sett.add(5)
print(sett)

sett.update({6,7,8})
print(sett)

for i in sett:
    print(i)

sett.remove(1)
print(sett)

sett.discard(1)
print(sett)

sett.pop()
print(sett)


sett.clear()
print(sett)


fruit=["apple","banana","mango"]
print("apple" in fruit)