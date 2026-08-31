def function_name():
    print("hello")
function_name()


def function_name(name):
    print("hello",name)
function_name("rimel")


def function_name(a,b):
    return a+b
add=function_name(4,2)
print(add)

def sq():
    return 200
sq()

def info(name,age):
    print(name,age)
info(name="rimel ahmed",age=23)

def square(x):
    return x*x
ss=square(6)
print(ss)

def mul(a,b):
    return a+b,a-b,a*b
x,y,z=mul(6,4)
print(x,y,z)