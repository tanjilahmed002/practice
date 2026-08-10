#student information

# name=input("enter your student name :")
# id=input("enter your student id :")
# department=input("enter your department :")
# semester=input("enter your semester :")
# age=int(input("enter your age :"))
# print(f"Name:{name}")
# print("ID :",id)
# print("Department :",department)
# print("semester :",semester)
# print("Age :",age)



#simple calculator

while True:
    print(" 1.Addition")
    print(" 2.Substraction")
    print(" 3.Multiplication")
    print(" 4.Division")

    
    inn=int(input("enter your choice & type 0 for end the loop :"))
    if inn==0:
        break
    if inn==1:
        num1=float(input("enter your num1 :"))
        num2=float(input("enter your num2 :"))
        Addition=num1+num2
        print("Addition :",Addition)
    elif inn==2:
        num3=float(input("enter your num3 :"))
        num4=float(input("enter your num4 :"))
        Substraction=num3-num4
        print("substraction :",Substraction)
    elif inn==3:
        num5=float(input("enter your num5 :"))
        num6=float(input("enter your num6 :"))
        Multiplication=num5*num6
        print("Multiplication :",Multiplication)
    elif inn==4:
        num7=float(input("enter your num7 :"))
        num8=float(input("enter your num8 :"))
        Division=num7/num8
        print("Division :",Division)
    else:
        print("invalid choice!try again.")

