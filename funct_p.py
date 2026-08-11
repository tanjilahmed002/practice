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




def function_name():
    print("hello")
function_name()

def function_name(name):
    print(name)
function_name("rimel")

def function_name(a,b):
    return a+b
add=function_name(3,4)
print(add)

def function_name():
    return 100
print(function_name())

def function_name(name,age):
    print(name,age)
function_name("rimel ahmed",23)

def function_name(name,age):
    print(name,age)
function_name(name="rimel ahmed",age=24)

def square(x):
    return x*x
result=square(3)
print(result)

def greet():
  print("Hello,welcome")
greet()

def greet(name):
  print(name)
name=input("enter your name :")
greet(name)

def add(a,b):
  return a+b

a=int(input("enter first num :"))
b=int(input("enter your second number :"))
sum=add(a,b)
print(sum)

def mul(a,b):
  return a+b,a-b,a*b,a/b
a=int(input("enter your first number :"))
b=int(input("enter your second number :"))
w,x,y,z=mul(a,b)
print(w,x,y,z)


def check_even_odd(number):
  if number%2==0:
    print("even")
    
  else:
    print("odd")

number=int(input("enter your number :"))
check_even_odd(number)


def check_number(number):
  if number>0:
    print("positive")
  elif number<0:
    print("negetive")
  else:
    print("zero")
number=int(input("enter your number :"))
check_number(number)

def rectangle(length,width):
  area=length*width
  return area

length=float(input("enter your length :"))
width=float(input("enter your width :"))
add=rectangle(length,width)
print(add)

def rectangle(length,width):
  return length*width
area=rectangle(4,5)
print(area)