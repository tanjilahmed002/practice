num=[1,2,3,4,5,6,7,1,2,1,1,2,4,5,3]
fruit=["apple",'mango',"banana"]
print(num.count(1))

print(fruit.index("banana"))

for i in range(len(num)):
    if num[i]==1:
        print("found at :",i)

unique=[]
for i in num:
    if not unique:
        unique.append(i)
    for j in unique:
        print(i,"appears at :",num.count(i))



class Bank:
    def __init__(self):
        self.__balance=500
    def get_balance(self):
        return self.__balance
    def set_balance(self,amount):
        if amount>0:
            self.__balance=amount
        else:
            print("invalid balance")
b=Bank()
print(b.get_balance())
b.set_balance(1000)
print(b.get_balance())


