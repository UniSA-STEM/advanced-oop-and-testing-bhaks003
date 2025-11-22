'''
File: reptile.py
Description: defines the repltile class, inheriting from Animal abstract class. consist of all repltiles in the zoo.
Author: Krish Bhadani
ID: 110429045
Username: bhaks003
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

class Reptile(Animal):
    # this reptile class inherits from an abstract Animal base class can call parent class as well
    def __init__(self, species, name, age, diet):  # this class will represent all the reptile in the zoo and also define their specific traits
        super().__init__(species, name, age ,diet, "reptile")

    def make_sound(self):
        """
            overiding the method passed from the parent class and changing according to child class need
            in this scenario it will the display the name species and sound bird's make
        """
        return self.get_name() + " the " + self.get_species() + " makes hisss or growls quietly"

    """
        orviding of the abstract daily_care method 
        returns the string stating about the daily care needed
    """
    def daily_care(self):
        return self.get_name() + " requries a dry arera, warm and temperature control system as well."


# snake = Reptile("Python", "Nagin", 4, "Rats")
# print(snake.make_sound())
# print(snake.daily_care())

