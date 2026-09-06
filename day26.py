fruit=["banana","mango","apple"]
print("apple" in fruit)

if "apple" in fruit:
    print("found")
else:
    print("not found")


num=[1,2,3,4,5,6,7,8,9,1,2,1,1,2,3,4,5,4,1,2]
for i in num:
    if i==1:
        print("found")
    else:
        print("not found")


print(num.count(1))
print(fruit.index("apple"))

for i in range(len(num)):
    if num[i]==1:
        print("founad at :",i)