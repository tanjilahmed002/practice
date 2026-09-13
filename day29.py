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