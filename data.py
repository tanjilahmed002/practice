fruits=["apple",'mango',"banana"]
if "apple" in fruits:
    print("found")
else:
    print("not found")

print("apple" in fruits)

num=[1,2,3,4,5,6,7,8,9,1,1,2,1,4,5]
for i in num: 
    if i==1:
        print("found")
    else:
        print("not found")

print(fruits.index("banana"))

for i in range(len(num)):
    if num[i]==1:
        print("found at :",i)

while True:
    search=input("enter your choice :").lower()
    if search=="end":
        break
    if search in fruits:
        print("found")
    else:
        print("not found")


print(num.count(1))

count=0
for i in num:
    if i==1:
        count=count+1
print(count)


listtt=[]
for n in num:
    if not  listtt:
        listtt.append(n)
for i in listtt:
    print(i,"appears",num.count(i))