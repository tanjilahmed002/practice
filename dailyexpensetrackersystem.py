#dailyexpensetracker
print("welcome to daily expense tracker")

budget=int(input("enter your daily budget :"))

expense=int(input("enter your daily expense :"))
total_expense=0
store_date=[]
while expense>0:
    category=input("enter your category :")
    amount=int(input("enter your amount :"))
    expense=expense-1
    store_date.append([category,amount])

    total_expense=total_expense+amount


for i in store_date:
    print(i)




print("total expense :",total_expense)

if total_expense  > budget:
    print("budget exceeded")
else:
    print("you are within budget")
