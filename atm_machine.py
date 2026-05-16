print("welcome to atm machine")

balance=1000

while True:
    choice=int(input("enter your choice "))
    if choice==1:
        print("Your current balance is :",balance)


    elif choice==2:
        print("withdraw")
        withdraw_balance=int(input("enter your withdraw balance :"))
        if withdraw_balance>balance:
            print("insufficient balance")
        else:
            withdraw=balance-withdraw_balance
            print("After withdraw your current balance is :",withdraw)
    elif choice==3:
        print("deposite")
        deposite_balance=int(input("enter your deposite balance :"))
        deposite=balance+deposite_balance
        print("After deposite your current balance is :",deposite)

    else:
        print("Enter 1,2,3 for your choice otherwise it will be invalid")

    #exit
    exit_button=input("Do you want repeat it again enter (yes/no)")
    if exit_button=="yes":
        print("continue")
    else:
        print("exit!")
        break


            
