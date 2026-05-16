import random
print("Welcome to number guessing game!")
secret_number=random.randint(1,10)
chance=5
while chance>0:
    print("ramaining chance:",chance)
    guess=int (input("Enter guess numberr 1 to 10:"))

    if guess==secret_number:
        print("congratulation!you guess correct number")
        break
    elif  guess>secret_number:
        print("to high try again")
    else:
        print("to low try again")  
    chance=chance-1 
       
              
if chance==0:
    print("you are ran out of chance!The correct was",secret_number)         