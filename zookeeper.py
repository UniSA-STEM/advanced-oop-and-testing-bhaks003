'''
File: zookeeper.py
Description: this is zookeeper class, in inherits from staff, responsible to feed and clean the animals and enclosure
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
    def __init__(self, name, role="Zookeeper"):
        super().__init__(name, role)

    # this function is return the string statement about zookeeper feeding the animal
    def feed_animal(self, animal):
        return f"{self.get_name()} is feeding animal {animal.get_name()} which is {animal.get_species()}"

    """
    this method will return the string statement of cleaning the enclosure will make the enclosure liveable again
    """
    def clean_enclosure(self, enclosure):
        status = enclosure.clean()
        return f"{self.get_name()} is cleaning enclosure {enclosure.clean()}. {status}"
