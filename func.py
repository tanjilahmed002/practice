def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

def get_number():
    num1=float(input("enter your number 1 :"))
    num2=float(input("enter your number 2 :"))
    return num1,num2

def calculators():
    while True:
        print("1.Addition")
        print("2.Substraction")
        print("3.Multipication")
        print("4.Division")
        print("5.Exit")
        choice=input("enter your choice & type 5 for exit the loop :")
        if choice=="5":
            print("exit the program")
            break
        if choice in ["1","2","3","4"]:
            a,b=get_number()
        if choice=="1":
            print("Addition :",add(a,b))
        elif choice=="2":
            print("Substraction :",sub(a,b))
        elif choice=="3":
            print("Multipication :",mul(a,b))
        elif choice=="4":
            print("Division :",div(a,b))
        else:
            print("invalid choice try again latter")
if __name__ == "__main__":
    calculators()