print("welcome to student performance requirement system")
student=int(input("enter student number :"))
while student>0:
    name=input("enter student name :")
    total_mark=float(input("enter total mark :"))
    obtain_mark=float(input("enter obtain mark :"))
    student=student-1

    percentage=(obtain_mark/total_mark)*100

    if percentage>=90:
        Grade="A+"
    elif percentage>75:
        Grade="A"
    elif percentage>60:
        Grade="B"
    elif percentage>40:
        Grade="C"
    else:
        Grade="Faill"


    store_data=[]
    store_data.append([name,total_mark,obtain_mark,percentage,Grade])
    for i in store_data:
        print(i)

       




