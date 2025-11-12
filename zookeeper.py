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
    """
    in the zookeeper class which inherit from staff class
    it represent a zoo staff who takes care of feeding and cleaning the enclosure
    for daily purpose
    """
    def __init__(self, name):
        super().__init__(name, "Zookeeper")

    # this function is return the string statement about zookeeper feeding the animal
    def feed_animal(self, name):
        return f"{self.get_name()} is feeding animal {animal.get_name()} which {animal.get_species()}"

    """
    this method will return the string statement of cleaning the enclosure will make the enclosure liveable again
    """
    def clean_enclosure(self, enclosure):
        return f"{self.get_name()} is cleaning enclosure {enclosure.clean()}"
