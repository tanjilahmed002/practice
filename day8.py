tupple=(1,2,3,4,5)
print(tupple)
for i in tupple:
  print(tupple)

print(tupple[2:3])

dicc={
  "name":"rimel",
  "age":23
}
for key in dicc:
  print(key)

for value in dicc.values():
  print(value)

for key,value in dicc.items():
  print(key,value)

print(dicc.get("name"))
dicc["age"]=24
print(dicc)
dicc.update({"name":"tanjil","age":23})
print(dicc)

di={
  "s1":{"name":"rimel","age":24},
  "s2":{"name":"tanjil",'age':25}
}
for id,info in di.items():
  print(id)
  for k,v in info.items():
    print(k,v)