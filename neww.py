#step2:program introduction
print("Welcome to daily life problem solver toolkit")

#menusystem
while True:
    print("Enter 1 for sum calculator")
    print("enter 2 for Even or Odd checker")
    print("Enter 3 for Maximum finder")
    pres=int(input("Enter your choice : "))

    #sum calculator

    if pres==1:
        num1=float(input("Enter number1 : "))
        num2=float(input("Enter number2 : "))
        sum=num1+num2
        print("Sum calculation : ",sum)


    #even or odd checker
    # 
    elif pres==2:
        number=int(input("Enter your number : "))
        if number%2==0:
            print("Even")
        else:
            print("Odd")   


    elif pres==3:
        value1=float(input("enter your value1 : "))
        value2=float(input("Enter your value2 : "))
        value3=float(input("Enter your value3 : "))
        if value1 > value2 and value1 > value3:
            value="value 1 is larger"
        elif value2 > value1 and value2 > value3:
            value="value 2 is larger" 
        else:
            value="value 3 is larger"
        print("The largest number is : ",value)   

    else:
        print("Invalid.Please enter 1,2,3")                       

    #repeat
    again=input("Enter your choise  do you want to reat it (yes or no): ")
    if again =="yes":
        print("Thank you.Now use it again")
    else:
        print("Thank you for using it")  
        break  
       