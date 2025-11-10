'''
File: reptile.py
Description: A brief description of this Python module.
Author: Krish Bhadani
ID: 110429045
Username: bhaks003
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

class Reptile(Animal):
    def __init__(self, species, name, age, diet):
        super().__init__(species, name, age ,diet, "reptile")

    def make_sound(self):
        return self.get_name() + "the" + self.get_species() + "makes hisss or growls quietly"

    def daily_care(self):
        return self.get_name() + "requries a dry arera, warm and temperature control system as well."
