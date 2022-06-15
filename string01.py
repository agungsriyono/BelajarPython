from ast import While


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
print("Agung Sriyono")

n = 7
i = 0
sum = 0

while i <= n:
    sum = sum + i
    i += 1    # update counter

for i in range(3):
    print(i)


print(sum)
