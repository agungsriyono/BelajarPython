f = open("demofile2.txt", "w") # w jadi replace, a cuman append
f.writelines("Now the file has more content!")
f.writelines("\n")
f.writelines("Now the file has more content- check!")
f.close()

