fruit=['mango',"apple","banana"]
print("apple" in fruit)
if "apple" in fruit:
    print("found")
num=[1,2,3,4,5,6,7,1,2,1,2,2]
for i in num:
    if i==2:
        print("found")
    else:
        print("not found")


print(num.count(2))

print(num.index(2))

for i in range(len(num)):
    if num[i]==2:
        print(num[i],"appears at",i)

while True:
    search=input("enter your choice :").lower()
    if search=="end":
        break
    if search in fruit:
        print("found")
    else:
        print("not found")

unique=[]
for i in num:
    if not unique:
        unique.append(i)
    for j in unique:
        print(num[i],"appeares in",num.count(i))
count=0
for i in num:
    if i==2:
        count=count+1
print(i,"count in",count)

dic={}
while True:
    key=input("enter your key :")
    if key=="end":
        break
    value=input("enter your value :")
    dic[key]=value

for key,value in dic.items():
    print(key,value)