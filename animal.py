'''
File: animal.py
Description: A brief description of this Python module.
Author: Krish Bhadani
ID: 110429045
Username: bhaks003
This is my own work as defined by the University's Academic Integrity Policy.
'''


from abc import ABC, abstractmethod
from health_record import HealthRecord

class Animal(ABC):
    def __init__(self, species, name, age, diet, category):
        self.__species = species
        self.__name = name
        self.__age = age
        self.__diet = diet
        self.__category = category
        self.__enclosure = []
        self.__health_records = []

    def get_category(self):
        return self.__category

    def get_species(self):
        return self.__species

    def get_name(self):
        return self.__name

    def feed(self):
        return self.__name + "the" + self.__species + "is eating" + self.__diet + "."

    def sleep(self):
        return self.__name + "the" + self.__species + "is sleeping calmly."

    def assing_enclosure(self, enclosure):
        self.__enclosure = enclosure

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def daily_care(self):
        pass

    def add_health_issues(self, description, severity, treatment):
        record = HealthRecord(description, severity, treatment)
        self.__health_records.append(record)

    def resolve_health_issue(self, index, notes):
        if index < 0 or index >= len(self.__health_records):
            raise IndexError("Invalid health record index")
        self.__health_records[index].resolve(notes)