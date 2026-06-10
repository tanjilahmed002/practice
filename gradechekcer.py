listt=[]
score=0
while True:
  mark=float(input("enter your mark and type end fot=r stop the loop :"))
  if mark==0:
    break
  listt.append(mark)

summ=sum(listt)
lenth=len(listt)
avg=summ/lenth
print("suma of list :",summ)
print("lenth of list :",lenth)
print("avg of this list :",avg)

if avg>=90:
  grade="A+"
  if avg>=85:
    grade="High A"
  elif avg>=80:
    grade="low A"
  else:
      grade="A"
elif avg>=70:
  grade="B"
elif avg>=60:
  grade="C"
elif avg>=50:
  grade="D"
elif avg>=40:
  grade="E"
else:
  grade="fail"
print("Grade :",grade)