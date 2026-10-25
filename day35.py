print("hello world")

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

def get_return():
    return 100
print(get_return())

def info(name,age):
    print(name,age)
info(name="rimel",age=23)


def student(name,age):
    print(name,age)
student("rimel",23)

def square(x):
    return x*x
addd=square(4)
print(addd)


def mult(a,b):
    return a-b,a+b,a*b,a/b
w,x,y,z=mult(5,3)
print(w,x,y,z)