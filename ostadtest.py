print("welcome to university admission system")

#input

Name=input("Enter your name : ")
Age=int(input("Enter your age : "))
GPA=float(input("Enter your  gpa : "))
Score=float(input("Enter your score :"))

#age check

if Age<18:
    print("not eligible for admission due to age")
else:
    print("age requirement satisfied")


#gpa evaluation


if GPA>=4.5:
    gpa="excelent gpa"
elif GPA>=3.5:
    gpa="good gpa"
elif GPA >=2.5:
    gpa="avarage"
else:
    gpa="low gpa" 
print("GPA : ",gpa)  

#admission decision

if GPA>=3.5 and Score>=70:
    Admission_status="Yes"
    print("congratulation you are admitted")
else:
    Admission_status="Not" 
    print("soryy,you are not admitted")


#finally summary

print("Name : ",Name)
print("Age : ",Age)
print("GPA : ",GPA)
print("Score : ",Score)
print("Admission status : ",Admission_status)       




