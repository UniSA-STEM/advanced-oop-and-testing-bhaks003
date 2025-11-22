'''
File: mammal.py
Description: Defines the mammal class, inheriting from Animal abstract class, representing all mammals in the zoo.
Author: Krish Bhadani
ID: 110429045
Username: bhaks003
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

class Mammal(Animal):
    # this mammal class inherits from an abstract Animal base class can call parent class as well
    # this class will represent all the mammal in the zoo and also define their specific traits
    def __init__(self, species, name, age, diet):
        super().__init__(species, name, age, diet, 'mammal')

    def make_sound(self):
        """
                overiding the method passed from the parent class and changing according to child class need
                in this scenario it will the display the name species and sound bird's make
        """
        return self.get_name() + " the " + self.get_species() + " is making a deep mammal sound"

    """
        orviding of the abstract daily_care method 
        returns the string stating about the daily care needed
    """
    def daily_care(self):
        return self.get_name() + " is required a land space which is warmth and has regular feeding"

# lion = Mammal("Lion", "Rocket", 5, "Meat")
# print(lion.make_sound())
# print(lion.daily_care())
