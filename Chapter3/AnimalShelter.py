class AnimalShelter:
    def __init__(self):
        self.cats = []
        self.dogs = []
        self.order = 0

    def AddAnimal(self, name, kind):
        kind = kind.lower()
        self.order += 1
        animal = {
            "order": self.order,
            "name": name,
            "kind": kind
        }
        if kind == "cat":
            self.cats.append(animal)
        elif kind == "dog":
            self.dogs.append(animal)

    def AdoptAnimals(self, Animal_list):
        if len(Animal_list) == 0:
            return None
        else:
            return  Animal_list.pop(0)

    def AdoptCats(self):
        return self.AdoptAnimals(self.cats)

    def AdoptDogs(self):
        return self.AdoptAnimals(self.dogs)

    def AdoptAny(self):
        if len(self.cats) == 0:
            return self.AdoptDogs()
        elif len(self.dogs) > 0 and self.cats[0]["order"] > self.dogs[0]["order"]:
            return self.AdoptDogs()
        else:
            return self.AdoptCats()

if __name__ == '__main__':
    Animal = AnimalShelter()
    Animal.AddAnimal("Tom", "cat")
    Animal.AddAnimal("Husky", "dog")
    Animal.AddAnimal("Jack", "dog")

    print(Animal.cats)
    print(Animal.dogs)

    animalreturn = Animal.AdoptDogs()

    print(animalreturn)

    print(Animal.AdoptAny())