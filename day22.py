def function_name():
    print("hello")
function_name()


def function_name(name):
    print("hello",name)
function_name("rimel")

def function_name(a,b):
    return a+b
add=function_name(3,2)
print(add)

def function_name():
    return 100
print(function_name())

def function_name(name,age):
    print(name,age)
function_name(name="rimel ahmed",age=23)


def function_name(x):
    return x*x
add=function_name(4)
print(add)

def function_name(a,b):
    return a+b,a-b,a*b
x,y,z=function_name(5,4)
print(x,y,z)



listt=[1,2,3,4,5]
print(listt)

for i in listt:
    print(i)

listt.append(6)
print(listt)

listt.insert(6,7)
print(listt)

listt.remove(7)
print(listt)
listt.pop(4)
print(listt)
listt.clear()
print(listt)

tupple=(1,2,3,4)
print(tupple)
for i in tupple:
    print(i)
print(tupple[1:2])