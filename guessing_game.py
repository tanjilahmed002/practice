import random
print("welcome to number guessing game!")
otp=random.randint(1,10)
count=0
while count<5:
    guess=int(input("enter your number & end to stop :"))
    if guess==otp:
        print("congratulation you are correct.")
        break
    elif guess>otp:
        print("you are too high")
    else:
        print("you are too low")
        count=count-1
else:
    print("try again latter")


