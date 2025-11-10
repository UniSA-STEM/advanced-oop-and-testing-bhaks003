'''
File: enclosure.py
Description: A brief description of this Python module.
Author: Krish Bhadani
ID: 110429045
Username: bhaks003
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Enclosure:
    def __init__(self, name, environement_type, size_sqkm, animal_type):
        self.__name = name
        self.__environement_type = environement_type
        self.__size_sqkm = size_sqkm
        self.__animal_type = animal_type
        self.__cleanliness_level = "Clean"
        self.__animals = []

    def get_cleanliness_level(self):
        return self.__cleanliness_level

    def clean(self):
        self.__cleanliness_level = "Clean"
        return f"{self.__name} has been fully cleaned"



    def add_animal(self, animal):
        self.__animals.append(animal)

    def remove_animal(self, name):
        for animal in self.__animals:
            if animal.get_name().lower() == name.lower():
                self.__animals.remove(animal)
                return f"{name} has been remoed from the {self.__name} enclosure."
        return f"{name} not found  in the {self.__name} enclosure."

    def list_animals(self):
        if not self.__animals:
            return f"THere are no animals found in the {self.__name} enclosure."
        result = ""
        for animal in self.__animals:
            result += animal.get_name() + " (" + animal.__get_species() + ")\n"
        return result
