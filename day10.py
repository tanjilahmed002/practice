print("welcome to my practice season")
#mark=float(input("enter your mark :"))
listt=[]
sum_of_mark=0
while True:
    mark=float(input("enter your mark & type end for stop the loop :"))
    if mark==00:
        break
    listt.append(mark)

sum_of_mark=sum(listt)
length=len(listt)
avg=sum_of_mark/length
print(avg)

if avg>80:
    grade="A+"
elif avg>70:
    grade="A"
elif avg>60:
    grade="B"
elif avg>50:
    grade="C"
elif avg>40:
    grade="Pass"
else:
    grade="Fail"
print("your result is :",grade)

