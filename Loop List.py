print("#1")
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
 

print("#2")
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

print("#3")
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

print("#4")
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]