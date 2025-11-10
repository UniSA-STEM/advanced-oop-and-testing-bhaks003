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

