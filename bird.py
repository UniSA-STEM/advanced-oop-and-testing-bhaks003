'''
File: bird.py
Description: Defines the bird class, inheriting from abstract animal classes, which represents all the birds in the zoo.
Author: Krish Bhadani
ID: 110429045
Username: bhaks003
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

class Bird(Animal):
    #this bird class inherits from an abstract Animal base class can call parent class as well
    # this class will represent all the bird in the zoo and also define their specific traits
    def __init__(self, species, name, age, diet):
        super().__init__(species, name, age, diet, "bird")

    def make_sound(self):
        """
        overiding the method passed from the parent class and changing according to child class need
        in this scenario it will the display the name species and sound bird's make
        """
        return self.get_name() + " the " + self.get_species() + " makes a sound squirk or squawks"

    """
    orviding of the abstract daily_care method 
    returns the string stating about the daily care needed
    """
    def daily_care(self):
        return self.get_name() + " requires a arial enclosure, clean perches and fresh water"

# parrot = Bird("Parrot", "James", 2, "Seeds")
# print(parrot.make_sound())
# print(parrot.daily_care())

