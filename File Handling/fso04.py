import os

 

cwd = os.getcwd()
print("Current working directory:", cwd)

x = "-----------------------------------\n"
x+= " DAFTAR PENYIMPANAN BARANG         \n"
x += "-----------------------------------\n"
for i in range(10):
    x += str(i+1) + "\n" 
x += "-----------------------------------\n"


print(x)


