thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])


thistuple = ("apple", "banana", "cherry")
if "banana" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")


x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)


# katanya gak bisa diubah, tapi tuple + tuple bisa...
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)


# Ngakalin ngerubah tuple, diubah ke list dulu baru dibuat tuple lagi
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# packing
fruits = ("apple", "banana", "cherry")

# unpacking
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

print("--------------asterik")
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

print("--------------asterik di tengah")
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)


tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)