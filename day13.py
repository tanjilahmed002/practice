length=float(input('enter your length :'))
width=float(input("enter your width :"))
area=length*width
print("here is the area :",area)

#age

current_year=2026
age=int(input("enter your birth year :"))
current_age=current_year-age
print("your age is :",current_age)


#celcius to fahrenhait

c=float(input("enter celcius :"))
f=(c*9/5)+32
print("fahrenhait :",f)

#pass or faill

marks=float(input('enter your mark :'))
if marks>=40:
    print("pass")
    
    if marks>=80:
        grade="a+"
    elif marks>=70:
        grade="a"
    elif marks>=60:
        grade="A-"
    elif marks>=50:
        grade="b"
    else:
        grade="c"
else:
    grade="fail"
print("your grade is :",grade)




for i in range(1,20+1):
    print(i)
sum=0
for i in range(1,100+1):
    sum=sum+i
print(sum)


num=int(input("enter your number :"))
for i in range(1,10+1):
    print(i,"*",num,"=",i*num)

even=0
odd=0
for i in range(1,100+1):
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print("even :",even)
print("odd :",odd)


