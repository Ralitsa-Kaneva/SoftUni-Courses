class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        message = ""
        if species == "mammal":
            mammals_string = ", ".join(self.mammals)
            message = f"Mammals in {self.name}: {mammals_string}\nTotal animals: {self.__animals}"
        elif species == "fish":
            fishes_string = ", ".join(self.fishes)
            message = f"Fishes in {self.name}: {fishes_string}\nTotal animals: {self.__animals}"
        elif species == "bird":
            birds_string = ", ".join(self.birds)
            message = f"Birds in {self.name}: {birds_string}\nTotal animals: {self.__animals}"
        return message


zoo1 = Zoo("Pernik")
zoo2 = Zoo("StaraPlanina")

zoo1.add_animal("fish", "Gertruda")
zoo2.add_animal("bird", "Gargo")


zoo_name = input()
zoo = Zoo(zoo_name)
lines = int(input())

for i in range(0, lines):
    animal_info = input().split(" ")
    species = animal_info[0]
    name = animal_info[1]
    zoo.add_animal(species, name)

species_to_print = input()

print(zoo.get_info(species_to_print))



