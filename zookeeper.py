'''
File: zookeeper.py
Description: A brief description of this Python module.
Author: Krish Bhadani
ID: 110429045
Username: bhaks003
This is my own work as defined by the University's Academic Integrity Policy.
'''

from staff import Staff

class Zookeeper(Staff):
    def __init__(self, name):
        super().__init__(name, "Zookeeper")

    def feed_animal(self, name):
        return f"{self.get_name()} is feeding animal {animal.get_name()} which {animal.get_species()}"

    def clean_enclosure(self, enclosure):
        return f"{self.get_name()} is cleaning enclosure {enclosure.clean()}"

