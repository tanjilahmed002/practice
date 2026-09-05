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


print(fruits.index("banana"))


print(fruits.count("banana"))
print(num.count(1))


for i in range(len(num)):
    if num[i]==1:
        print("found at :",i)


unique=[]
for j in num:
    if not unique:
        unique.append(j)
for i in unique:
    print(i,"appears",num.count(i))



print(fruits.count("banana"))
print(num.count(1))

print(fruits.index("mango"))

for i in range(len(num)):
    if num[i]==1:
        print("found at ",i)

for n in num:
    if not unique:
        unique.append(n)
for i in unique:
    print(i,"appears",num.count(i))


dict={
    "s1":{"name":"rimel","age":23,"mark":90},
    "s2":{"name":"tanjil","age":24,"mark":80}
}
print(dict)

for i,j in dict.items():
    print(i)
    for key,value in j.items():
        if key=="name":
            print(key,value)
        print(key,value)


dic={}
while True:
    key=input("enter your key :")
    if key=="end":
        break
    value=input("enter your value :")
    dic[key]=value

for i,j in dic.items():
    print(i,j)


def function_name():
    print("hello")
function_name()

def function_name(name):
    print("helo",name)
function_name("rimel")

def function_name(name,age):
    print( name,age)
function_name(name="rimel",age=23)

def function_name(a,b):
    return a+b
add=function_name(5,4)
print(add)