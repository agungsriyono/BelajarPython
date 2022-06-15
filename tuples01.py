print("#1")
thistuple = ("apple", "banana", "cherry")
print(thistuple)

print("#2")
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

print("#3")
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


print("#4")
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

print("#5")
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

print("#6")
thistuple = tuple(((("apple", "banana", "cherry")))) # note the double round-brackets
print(thistuple)










