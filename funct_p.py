def function_name():
    print("hello")
function_name()

def function_name(name):
    print("hello",name)
function_name("rimel")


def function_name(a,b):
    return a+b
add=function_name(2,3)
print(add)

def function_name():
    return 100

print(function_name())


def info(name,age):
    print(name,age)
info("rimel",23)

def student(name,age):
    print(name,age)
student(name="rimel ahmed",age=24)

def square(x):
    return x*x
ss=square(4)
print(ss)

def mul(a,b):
    return a+b,a-b,a*b,a/b
w,x,y,z=mul(5,4)
print(w,x,y,z)