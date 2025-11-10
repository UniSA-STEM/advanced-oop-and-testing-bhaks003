'''
File: enclosure.py
Description: A brief description of this Python module.
Author: Krish Bhadani
ID: 110429045
Username: bhaks003
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Enclosure:
    def __init__(self, name, environment_type, size_sqkm, animal_type):
        if not name:
            raise ValueError("Enclosure name cannot be empty.")
        if size_sqkm <= 0:
            raise ValueError("Enclosure size must be greater than 0.")
        if animal_type not in ["mammal", "bird", "reptile"]:
            raise ValueError("Allowed animal type must be one of: mammal, bird, reptile.")
        self.__name = name
        self.__environment_type = environment_type
        self.__size_sqkm = size_sqkm
        self.__animal_type = animal_type
        self.__cleanliness_level = "Clean"
        self.__animals = []

    def get_cleanliness_level(self):
        return self.__cleanliness_level

    def get_environment_type(self):
        return self.__environment_type

    def get_animal_count(self):
        return len(self.__animals)

    def clean(self):
        self.__cleanliness_level = "Clean"
        return f"{self.__name} has been fully cleaned."

    def add_animal(self, animal):
        if animal.get_category() != self.__animal_type:
            raise ValueError(
                f"Cannot add {animal.get_name()} ({animal.get_category()}) to {self.__name} enclosure. "
                f"Only {self.__animal_type}s allowed."
            )
        self.__animals.append(animal)

    def remove_animal(self, name):
        for animal in self.__animals:
            if animal.get_name().lower() == name.lower():
                self.__animals.remove(animal)
                return f"{name} has been removed from the {self.__name} enclosure."
        return f"{name} not found in the {self.__name} enclosure."

    def list_animals(self):
        if not self.__animals:
            return f"There are no animals found in the {self.__name} enclosure."
        result = ""
        for animal in self.__animals:
            result += animal.get_name() + " (" + animal.get_species() + ")\n"
        return result

    def __str__(self):
        return (
            f"Enclosure: {self.__name} | Type: {self.__animal_type} | "
            f"Environment: {self.__environment_type} | Size: {self.__size_sqkm} sq.km | "
            f"Animals: {self.get_animal_count()} | Cleanliness: {self.__cleanliness_level}"
        )


from mammal import Mammal
from bird import Bird

savannah = Enclosure("Savannah Plains", "Savannah", 0.8, "mammal")
lion = Mammal("Lion", "Simba", 5, "Meat")
giraffe = Mammal("Giraffe", "Melman", 7, "Leaves")

savannah.add_animal(lion)
savannah.add_animal(giraffe)

print(savannah)
print("Animals:")
print(savannah.list_animals())
print(savannah.clean())

aviary = Enclosure("Tropical Aviary", "Rainforest", 0.2, "bird")
parrot = Bird("Parrot", "Polly", 2, "Seeds")
aviary.add_animal(parrot)
print(aviary)
