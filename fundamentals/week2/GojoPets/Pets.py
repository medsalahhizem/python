class Pet:
    def __init__(self, name, type, tricks, health=100, energy=100):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 24
        print(f"{self.energy} is increasing by 5")
        
    def eat(self):
        self.health += 10
        self.energy += 5
        print(f"{self.energy} is increasing by 5 and {self.health}is increasing by 10")
        
    def play(self):
        self.health += 5
        print(f"{self.health} is increasing by 5")
        
    def noise(self):
        print(f"{self.name} the {self.type} is calling you")
        
class Dog(Pet):
    def __init__(self, name, tricks, health=100, energy=100):
        super().__init__(name, "Dog", tricks, health, energy)

    def noise(self):
        print(f"{self.name} the dog is barking")

