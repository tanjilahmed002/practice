fruit=["apple","mango","banana"]

print(fruit)

print("apple" in fruit)

if "apple" in fruit:
    print("found")
else:
    print("not found")

num=[1,2,3,4,5,1,1,1,2]
for i in num:
    if i==1:
        print("found")
    else:
        print("not found")


for i in range(len(num)):
    if num[i]==1:
        print(num[i],"appears at :",i)


print(num.count(1))

unique=[]
for i in num:
    if not unique:
        unique.append(i)
    for k in unique:
        print(num[i],"appears :",num.count(i))


dic={}
while True:
    key=input("enter your key :")
    if key=="end":
        break
    value=input("enter your value :")
    dic[key]=value
for key,value in dic.items():
    print(key,value)

liastt=[1,2,3,4,5]
print(liastt)

for i in liastt:
    print(i)

liastt.append(6)
print(liastt)

liastt.insert(6,7)
print(liastt)

liastt.remove(7)
print(liastt)

liastt.pop(5)
print(liastt)

liastt.clear()
print(liastt)

tupple=(1,2,3,4,"rimel")
print(tupple)

for i in tupple:
    print(i)

print(tupple[1:2])

dicc={
    "name":'rimel ahmed',
    "age":23
}
print(dicc)


for i in dicc:
    print(i)

for value in dicc.items():
    print(value)

for key,value in dicc.items():
    print(key,value)


dicc["name"]="rimel"
print(dicc)


del dicc["age"]
print(dicc)

dicc.clear()
print(dicc)

sett={1,2,3,4}
print(sett)

sett.add(5)
print(sett)

sett.update({6,7,8,10})
print(sett)