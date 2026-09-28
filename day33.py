fruit=["apple",'mango',"banana"]
print("apple" in fruit)
if "apple" in fruit:
    print("found")
else:
    print("not found")

num=[1,2,3,2,1,4,5,6,1,2,1]
for i in num:
    if i==1:
        print("found")
    else:
        print("not found")


print(num.count(1))

for i in range(len(num)):
    if num[i]==1:
        print(num[i],"appears in :",i)