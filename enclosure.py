'''
File: enclosure.py
Description: Defening the enclosure class, represents a zoo area where animals are kept.
Author: Krish Bhadani
ID: 110429045
Username: bhaks003
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Enclosure:
    """
    the class enclosure represent a physical area in a zoo where animals are kept.
    each enclosure has its environment type, size and animal category restrictions
    and cleanliness level. It will also have methods like adding, removing and listing animals.
    """
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
        self.__animals = [] #using a list to store all animals assigned to enclosure

    #using getters method
    def get_cleanliness_level(self):
        return self.__cleanliness_level

    def get_environment_type(self):
        return self.__environment_type

    def get_animal_count(self):
        return len(self.__animals)

    #peak enclosure actions
    def clean(self):
        """
        this will reset the cleanliness level to clean and will also display the appropriate message
        """
        self.__cleanliness_level = "Clean"
        return f"{self.__name} has been fully cleaned."

    """
    this add_animal method will be able to add an animal to the animals list
    if animal's category it same then only it will be able to add 
    """
    def add_animal(self, animal):
        if animal.get_category() != self.__animal_type:
            raise ValueError(
                f"Cannot add {animal.get_name()} ({animal.get_category()}) to {self.__name} enclosure. "
                f"Only {self.__animal_type}s allowed."
            )
        self.__animals.append(animal)
        return f"Added {animal.get_name()} to {self.__name}"

    """
    this method will remove an animal from the enclosure list if none found it will still display the message not found
    """
    def remove_animal(self, name):
        for animal in self.__animals:
            if animal.get_name() == name:
                self.__animals.remove(animal)
                print(f"{name} has been removed from the {self.__name} enclosure.")
        print(f"{name} not found in the {self.__name} enclosure.")

    # this method is will display the animals currently present  in the enclosure and also format how to will show.
    def list_animals(self):
        if not self.__animals:
            return f"There are no animals found in the {self.__name} enclosure."
        result = ""
        for animal in self.__animals:
            result += animal.get_name() + " (" + animal.get_species() + ")\n"
        return result

    def __str__(self): # string conversion method
        return (
            f"Enclosure: {self.__name} | Type: {self.__animal_type} | "
            f"Environment: {self.__environment_type} | Size: {self.__size_sqkm} sq.km | "
            f"Animals: {self.get_animal_count()} | Cleanliness: {self.__cleanliness_level}"
        )


# from mammal import Mammal
# from bird import Bird
#
# woodland = Enclosure("Black Woodlands", "Woodland", 0.8, "mammal")
# lion = Mammal("Lion", "Rocket", 5, "Meat")
# giraffe = Mammal("Giraffe", "Lambu", 7, "Leaves")
#
# woodland.add_animal(lion)
# woodland.add_animal(giraffe)
#
# print(woodland)
# print("Animals:")
# print(woodland.list_animals())
# print(woodland.clean())
#
# aviary = Enclosure("Tropical Aviary", "Rainforest", 0.2, "bird")
# parrot = Bird("Parrot", "Popat", 2, "Seeds")
# aviary.add_animal(parrot)
# print(aviary)
