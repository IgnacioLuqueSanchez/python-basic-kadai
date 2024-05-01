class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def check_adult(self):
        if self.age >= 20:
            print(f"{self.name} is an adult")
        else:
            print(f"{self.name} is not an adult")

human1 = Human("Nacho", 36)
human2 = Human("Pablo", 20)
human3 = Human("Kairen", 3)
human4 = Human("Ana", 10)

humans = [human1, human2, human3, human4]

for human in humans:
    human.check_adult()



