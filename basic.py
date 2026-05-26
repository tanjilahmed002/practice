# # dic={
# #     "name":"rimel",
# #     "age":23,
# #     "mark":80
# # }
# # 
# # print(dic)
# # for key in dic:
# #     print(key)

# # for value in dic.values():
# #     print(value)

# # for key,value in dic.items():
# #     print(key,":",value)


# dic={}
# dic["name"]="rimel"
# dic["age"]=23
# print(dic)
# print(dic["name"])
# print(dic.get("age"))
# dic["age"]=24
# print(dic["age"])
# dic.update({"name":"rimel ahmed","age":23})
# print(dic)
# del dic["age"]
# print(dic)
# dic.pop("name")
# print(dic)

# dic={
#     "s1":{"name":"rimel","age":23},
#     "s2":{"name":"tanjil","age":24}
# }
# print(dic)
# dic["s3"]={"name":"rahim","age":25}
# print(dic)
# for id,info in dic.items():
    
#     print(id)
#     for key,value in info.items():
#         if key=="name" and id=="s3":
#             print(value)

# sett={1,2,3,4,5,6,7}
# print(sett)
# for i in sett:

#     print(i,end=" ")

# sett.add(8)
# print(sett)
# sett.update({9,10,11,12,13})
# print(sett)

fruits=["banana","mango","apple"]
# print("apple" in fruits)
# if "apple" in fruits:
#     print("found")
# else:
#     print("not found")

# for i in fruits:
#     if i=="banana":
#         print("found")
#         break
#     else:
#         print("not found")
# num=[1,2,3,4,5,6,7,8]
# for i in num:
#     if i==3:
#         print("found")
        
#     else:
#         print("not found")


# fruits=["banana","mango","apple"]
# while True:
#     search=input("enter your choice & type end for stop the loop :").lower()
#     if search=="end":
#         break
#     if search in fruits:
#         print("found")
#     else:
#         print("not found")
# count=0
# num=[1,1,1,2,2,3,4,5,6,7,8,9]
# for i in num:
#     if i==1:
#         count=count+1
# print(count)

# dic={}
# while True:
#     key=input("enter your key :")
#     if key=="stop":
#         break
#     value=input("enter your value :")
#     dic[key]=value
# print(dic)

# def myname():
#     print("rimel")
# myname()

# def mynamee(name):
#     print(name)
# mynamee("tanjil ahmed rimel")

# def add(a,b):
#     return a+b
# result=add(2,3)
# print(result)

# def div(a,b):
#     print(a,b)
# div(a=12,b=10)
x=10
# def outer():
#     global x
#     x=100
#     print(x)
# outer()
# def inner():
#     x=100
#     print(x)
# inner()

# def outer():
#     x=10
#     def inner():
#         print(x)
#     inner()
# outer()
# def outer():
#     x=10
#     def inner():
#         nonlocal x
#         x=100
        
#     inner()
#     print(x)
# outer()

# import math
# print(math.e)
# print(math.sqrt(25))
# print(math.fabs(-10))
# print(math.factorial(5))
# print(math.pi)
# print(math.ceil(3.12))

#import random
# name=["rimel","tanjil","rahim","koushik"]
# random.choice(name)
# print(random.choice(name))
# print(random.sample(name,2))

import random
otp=random.randrange(10,50,5)
print("your pin is :",otp)