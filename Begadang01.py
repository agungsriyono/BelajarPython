print("#1")
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon","test"]
print(thislist)

print("#2")
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

print("#3")
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

print("#4")
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

print("#5")
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

print("#6")
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

print("#7")
thislist = ["apple", "banana", "cherry", "banana", "banana"]
thislist.remove("banana")
print(thislist)

print("#8")
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

print("#9")
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

print("#10")
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

print("#11")
thislist = ["apple", "banana", "cherry"]
del thislist
#print(thislist) Jadi error karena variable sudah tidak ada

