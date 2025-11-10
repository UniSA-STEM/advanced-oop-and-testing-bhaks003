'''
File: mammal.py
Description: A brief description of this Python module.
Author: Krish Bhadani
ID: 110429045
Username: bhaks003
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

class Mammal(Animal):
    def __init__(self, species, name, age, diet):
        super().__init__(species, name, age, diet, 'mammal')

    def make_sound(self):
        return self.get_name() + "the" + self.get_species() + "is making a deep mammal sound"

    def daily_care(self):
        return self.get_name() + "is required a land space which is warmth and has regular feeding"