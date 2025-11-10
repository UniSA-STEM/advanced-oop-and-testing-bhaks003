'''
File: bird.py
Description: A brief description of this Python module.
Author: Krish Bhadani
ID: 110429045
Username: bhaks003
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

class Bird(Animal):
    def __init__(self, species, name, age, diet):
        super().__init__(species, name, age, diet, "bird")

    def make_sound(self):
        return self.get_name() + "the" + self.get_species() + "makes a sound squirk or squawks"

    def daily_care(self):
        return self.get_name() + "requires a arial enclosure, clean perches and fresh water"

