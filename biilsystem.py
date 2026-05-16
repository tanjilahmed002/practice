print("welcome to bill systme")
total=0.0
count=0
running=True
while running:
  price=float(input("Enter your price And press 0 to stop the loop :"))
  if price==0:
    running=False
  elif price<0:
    print("invalid price")
  else:
    total=total+price
    count=count+1


if count==0:
  print("no purchase")
else:
  print("This is total : ",total)
  print("total count : ",count)
  #discount

  if total>=5000:
    discount=total*0.20
  elif total>=3000:
    discount=total*0.10
  else:
    discount=0.0
  after_discount=total-discount
  vat=after_discount*0.5
  final_bill=after_discount+vat

  print(".......Bill.......")
  print("After discount : ",after_discount)
  print("total vat(5%) : ",vat)
  print("final bill : ",final_bill)
