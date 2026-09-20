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