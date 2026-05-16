print("welcome to student score tracker")
scores=[]
while True:
  value=int(input("Enter your value (type 0 to stop):"))
  if value ==0:
    break
  
  scores.append(value)

#calculation    
total=sum(scores)
count=len(scores)
avg=total/count
  
#conditon for grading 
if avg>=40:
  if avg>=80:
    Grade="A+"
  elif avg>=70:
    Grade="B"
  elif avg>=60:
    Grade="C"
  elif avg>=50:
    Grade="D"
  else:
    Grade="E"
else:
    Grade="Faill"
#show all of this
print("---Result System---")
print("Score :",scores)
print("Total :",total)
print("Subject count :",count)
print("Aeverage :",avg)
print("Highest score :",max(scores))
print("Lowest score :",min(scores))  
print("Grade :",Grade)          

