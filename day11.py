mark=80
if mark>=50:
    print("pass")
else:
    print("fail")


dic={}
while True:
    key=input("enter your key :")
    if key=="end":
        break
    value=input("enter your value :")
    dic[key]=value
for key,value in dic.items():
    print(key,value)