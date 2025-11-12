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
    """
    abstract class representing an generic animal present in the zoo.
    all animals share will share core attributtes such as species, name, age, diet and category
    subclasses will implement make_sound() and daily_care() to define their unique behaviour
    """
    def __init__(self, species, name, age, diet, category):
        """
        Instantiate an animal with species, name, age, diet, and category attributes.
        creating an enclosure list
        and health record list
        """
        self.__species = species
        self.__name = name
        self.__age = age
        self.__diet = diet
        self.__category = category
        self.__enclosure = []
        self.__health_records = []

    # ----------------
    # using getters methods return info
    # -------------------
    def get_category(self):
        return self.__category

    def get_species(self):
        return self.__species

    def get_name(self):
        return self.__name

    def feed(self):
        """
        showcase about animal eating food
        return with a string which shows which animal is eating food
        """
        return self.__name + "the " + self.__species + " is eating " + self.__diet + "."


    """
    in this sleep method it will return the animal name which sleeping 
    """
    def sleep(self):
        return self.__name + "the " + self.__species + " is sleeping calmly."

    def assign_enclosure(self, enclosure):
        # assigning an enclosure to an animal according to category
        self.__enclosure = enclosure

    @abstractmethod
    def make_sound(self):
        # this abstract methodn will be inherited in the child class
        pass

    @abstractmethod
    def daily_care(self): #abstract method which will be implemented in child classes
        pass

    """
    Health Management methods
    """
    def add_health_issues(self, description, severity, treatment):
        # in this method animal's health record can be added which will save the desciption, severity, treatment given and date it was reported
        record = HealthRecord(description, severity, treatment, date_reported)
        self.__health_records.append(record)

    # this method will resolve the health recrod as resolved and will include the notes for future diagnose
    def resolve_health_issue(self, index, notes):
        if index < 0 or index >= len(self.__health_records):
            raise IndexError("Invalid health record index")
        self.__health_records[index].mark_resolved(notes)

    """
    has_serious_active_issues will tell us about the animal health severity which are high or serious
    it will return true if has an active health issue and false otherwise
    """
    def has_serious_active_issues(self):
        i = 0
        while i < len(self.__health_records):
            record = self.__health_records[i]
            if record.is_serious():
                return True
            i = i + 1
        return False

    def get_health_summary(self):
        summary = []
        #this method returns a list of summaries for all record associated with the animal
        for record in self.__health_records:
            summary.append(str(record))
        return summary

    #++++++++++++++++++++
    # String conversion method will display Name (Species, Category, age)
    #+++++++++++++++++++
    def __str__(self):
        return self.__name + " (" + self.__species + ", " + self.__category + ", age " + str(self.__age) + ")"