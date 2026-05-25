import math
print("welcome to shopping bill system")
count=0
total=0
running=True
while running:
    price=int(input("Enter your price :"))
    if price==0:
        running=False
        break
    elif price<0:
        print("invalid price")
    else:
        total=total+price
        count=count+1

if count==0:
    print("no item purchase.")
else:
    print("Total pice is :",total)
    print("Total item is :",count)


#discount

if total>=5000:
    discount=total*0.20
elif total>=3000:
    discount=total*0.10
else:
    discount=0

after_discount=total-discount

vat=after_discount*0.5
final_bill=after_discount+vat

print("-------Final Bill-------")
print(f"Discount :{discount}")
print(f"vat :{vat}")
print(f"final bill :{final_bill}")
