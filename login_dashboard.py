print("Welcome to login system")

count=3
marks=[]
while count>0:
    username=input("Enter your user name :")
    password=input("enter your password :")
    count=count-1
    if username=="rimel" and password=="573":
        #break
        
        while True:
            print("---Dashboard Menu---")
            print("1. Add mark")
            print("2. Show Total marks")
            print("3. Show Average Marks")
            print("4. Show Highest Marks")
            print("5. Exit")
            option=int(input("enter your option :"))
            if option==1:
                mark=int(input("enter your mark :"))
                marks.append(mark)
                for i in marks:
                    print(f"Marks :{i}")
                    
               
            elif option==2:
                total_marks=sum(marks)
                print("Total marks :",total_marks)

            elif option==3:
                length=len(marks)
                avg=total_marks/length
                print("show Average Marks :",avg)
            elif option==4:
                highest_mark=max(marks)
                print("Show highest marks :",highest_mark)
            elif option==5:
                print("Thank you !")
                break
            else:
                print("choice 1,2,3,4,5 . Otherwise it will be invalid !")        


                 




        
