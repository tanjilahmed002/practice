import random
print("welcome to number guessing game")
secret_number=random.randint(1,10)
chance=5
while True:
    num=int(input("Enter your number :"))
    if num==secret_number:
        print("Congratulation!you are correct.")
        break
    elif num>secret_number:
        print("you are to high !")
    else:
        print("you are too low !")
    chance=chance-1
else:
    print("please try again !")
