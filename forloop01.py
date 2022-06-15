fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

print("----------------2")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

print("----------------3")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

print("----------------4")
for x in range(6):
  print(x)

print("----------------5")
for x in range(2, 5):
  print(x)

print("----------------6")
for x in range(2, 30, 3):
  print(x)

