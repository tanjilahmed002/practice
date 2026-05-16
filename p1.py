#question 2


print("welcome to employe performance system")

#input


employe_name=input("enter your name : ")
years=int(input("enter your years : "))
score=float(input("enter your score : "))
monthly_salary=float(input('enter your monthly salary : '))


#experience check

if years>=5:
    print("senior employer")
else:
    print("junior employer")


#performance grade


if score>=85:
    sc="A"
elif score>=70:
    sc="B"
elif score>=50:
    sc="C"
else:
    sc="F"    
print("Score : ",sc)

#bonous condition

if score>=60 and years>=3:
    bonous=0.20
elif score>=60:
    bonous=0.10
else:
    bonous=0.00
bounous_amount=monthly_salary*bonous
total_salary=monthly_salary+bounous_amount

print("name : ",employe_name)
print("score :",score)
print("Bonous amount :",bounous_amount)
print("total salary :",total_salary)




