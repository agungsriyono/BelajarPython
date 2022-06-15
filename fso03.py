#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

f = open("demofile2.txt", "r")
print(f.readline(1))
f.close()

print("------------")

f = open("demofile2.txt", "r")
i=0
for x in f:
    if i==2:
        print(x)
    i += 1