print("welcome to mini result calcultor!")
name=input("enter your name :")
sub1=float(input("enter your sub1 mark :"))
sub2=float(input("enteryour sub2 mark :"))
sub3=float(input("enter your sub3 mark :"))
sub4=float(input("enter your sub4 mark :"))
sub5=float(input("enter your sub5 mark :"))
total_mark=sub1+sub2+sub3+sub4+sub5
avg=total_mark/5
print("Total mark :",total_mark)
print("Average mark :",avg)
if avg>=40:
    if avg>=80:
        grade="A+"
    elif avg>=70:
        grade="A"
    elif avg>=60:
        grade="B"
    elif avg>=50:
        grade="C"
    else:
        grade="D"
else:
    grade="F"

print(f"your grade is {grade}")