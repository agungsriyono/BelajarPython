

class Sadboy :
    def __init__(self, ayang, randa):
        self.ayang = ayang 
        self.randa = randa 
    def merintih(self):
        print("Merenungi " + self.ayang)

Ucup = Sadboy("novia","neneng gubrag")

Ucup.randa = "Gadis Manglayang"

print(Ucup.ayang)
print(Ucup.randa)
Ucup.merintih()