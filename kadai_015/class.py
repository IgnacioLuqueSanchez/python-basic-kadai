class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printinfo(self):
        print("Name:", self.name)
        print("Age:", self.age)


    
Nacho = Human("Nacho", 36)
Pablo = Human("Pablo", 32)


Nacho.printinfo()
Pablo.printinfo()