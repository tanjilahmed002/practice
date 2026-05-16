print("welcome to smart task repetition system")

#program introduction

task_name=input("Enter your task name : ")
repeat=int(input("enter your times : "))

#using a for loop

for i in range(1,repeat+1):
    print(f"task {i} : study python completed")

#countdown using while loop

countdown=int(input("Enter your countdown number : "))
while countdown>0:
    print(countdown)
    countdown=countdown-1


#neested loop advanced

seasons=["morning","evening"]
for season in seasons:
    for task in range(1,4):
        print(f"{season} task {task}")