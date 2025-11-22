'''
File: veterinarian.py
Description: defining the vetarinarian class, which is inheriting from staff, responsible to maintain health record for animals
Author: Krish Bhadani
Author: Krish Bhadani
ID: 110429045
Username: bhaks003
This is my own work as defined by the University's Academic Integrity Policy.
'''

from staff import Staff

"""
the veterinarian class inherits from the base staff class
this is a for vet who performs health checks on animal
"""
class Veterinarian(Staff):
    def __init__(self, name, role="Veterinarian"):
        super().__init__(name, role)

    def conduct_checkup(self, animal, description, severity, treatment, date_reported):
        """
        method will perform health checks on animal and create a health record if none found 
        it will store the description, severity, treatment and date_reported for each animal 
        """
        animal.add_health_issues(description, severity, treatment, date_reported)
        print(f"{self.get_name()} Recorded new health issue for {animal.get_name()}: {description} {severity}")
