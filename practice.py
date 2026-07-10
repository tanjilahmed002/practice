#even or odd chekcer

while True:
  num=int(input("enter your number :"))
  if num==00:
    break
  if num%2==0:
    print("Even")
  else:
    print("odd")


#positive negetive zero checker

while True:
  inn=int(input("enter your number :"))
  if inn==0:
    break
  if inn>0:
    print("positive")
  elif inn<0:
    print("negetive")
  else:
    print('zero')

#largest three number

while True:
  num1=int(input("enter your number 1 :"))
  if num1==0:
    break
  num2=int(input('enter your number 2 :'))
  num3=int(input('enter your number 3 :'))

  if num1>num2 and num1>num3:
    print("num1 is largest ")
  elif num2>num1 and num2>num3:
    print("num2 is largest")
  else:
    print("num3 is largest")


#multipication
num=int(input("enter your number :"))
for i in range(1,11):
  print(i,"*",num,"=",i*num)

#sum of number
count=0
num=int(input("enter your number :"))
for i in range(1,num):
  count=count+i
  print("num is :",count)
  