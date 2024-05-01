class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def check_adult(self):
        if self.age >= 20:
            print(f"{self.name} is an adult")
        else:
            print(f"{self.name} is not an adult")

Human1 = Human("Nacho", 36)
Human2 = Human("Pablo", 20)
Human3 = Human("Kairen", 3)
Human4 = Human("Ana", 10)

Humans = [Human1, Human2, Human3, Human4]

for Human in Humans:
    Human.check_adult()



