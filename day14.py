print("welcome to daily life tracker program")

name=input("nter your name :")
available_hour=float(input("enter your daily available hour :"))
daily_budget=float(input("enter your daily budget :"))


#daily activity 
study_python=float(input("enter your study python :"))
practice_python=float(input("enter your practice python :"))
other_activities=float(input("enter your oither activities :"))

total_activities=study_python+practice_python+other_activities


#expense 

food=float(input("enter your food expense :"))
transport=float(input("enter your transport expesne :"))
other=float(input("enter your other epense :"))

total_daily_expense=food+transport+other

remaining_budget=daily_budget-total_daily_expense
#time planning check

if total_activities>available_hour:
    print("you have planned more hours than available")
else:
    print("your daily plan is realistic")


#budget check

if total_daily_expense>daily_budget:
    print("you have exceded your daily budget")
else:
    print("you are within your daily budget ")


print("Name :",name)
print("Total planned hour :",total_activities)
print("Available :",total_daily_expense)
print("Remaining budget :",remaining_budget)