

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)


thisset = {"apple", "banana", "cherry", "apple"}
for x in thisset:
  print(x)



thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

print("perintahnya Update tapi malah ADD")
# perintahnya Update tapi malah ADD
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)


thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)


thisset = {"apple", "banana", "cherry"}
#thisset.discard("banana")
thisset.remove("banana")
print(thisset)


thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)


# clear
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)


