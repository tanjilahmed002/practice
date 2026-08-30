print("welcome to daily expense tracker")
dic={}
listt=[]
while True:
    print("1.Add expense")
    print("2.view expense")
    print("3.update expense")
    print("4.search expense")
    print("5.Delete expense")
    print("6.total expense")
    choice=input("enter your choice & type 7 for end the loop :")
    if choice=="7":
        break
    if choice=="1":
        id=input("enter your id :")
        name=input("enter your name :")
        amount=float(input("enter your amount :"))
        category=input("enter your category :")
        date=input("enter your date :")
        dic={
            "id":id,
            "name":name,
            "amount":amount,
            "category":category,
            "date":date
        }
        listt.append(dic)
        print("expense added successfully")
    elif choice=="2":
        for i in listt:
            print("======Expense======---")
            print("Id       :",i["id"])
            print("name     :",i["name"])
            print("Amount   :",i["amount"])
            print("Category :",i["category"])
            print("Date     :",i["date"])
            print("======expense======")
        
        
    elif choice=="3":
        choices_id=input("enter your id for update :")
        for i in listt:
            if i["id"]==choices_id:
                names=input("enteryour updated name :")
                amounts=input("enter your updated amounts :")
                categories=input("enter your updated categories :")
                updated_date=input("enter your updated date :")
                i.update({"name":names,"amount":amounts,"category":categories,"date":updated_date})
                print("updated successfully")
            else:
                print("invalid id")

        
        
    elif choice=="4":
        search=input("enter your id for search :")
        for i in listt:
            if i["id"]==search:
                print("Id :",i["id"])
                print("name :",i["name"])
                print("Amount :",i["amount"])
                print("Date :",i["date"])
            else:
                print("invalid")
        
    elif choice=="5":
        print("delete expense")
    elif choice=="6":
        print("total expense")
    else:
        print("invalid choice")
    