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

if "apple" in fruit:
    print("found")
else:
    print("not found")

num=[1,2,3,4,5,1,2,3,1,2,1]
for i in num:
    if i==1:
        print("found")
    else:
        print("not found")


print(num.count(1))

print(num.index(1))

for i in range(len(num)):
    if num[i]==1:
        print(i)