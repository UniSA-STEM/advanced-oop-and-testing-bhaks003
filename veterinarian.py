'''
File: veterinarian.py
Description: A brief description of this Python module.
Author: Krish Bhadani
ID: 110429045
Username: bhaks003
This is my own work as defined by the University's Academic Integrity Policy.
'''

from health_record import HealthRecord
from staff import Staff

"""
the veterinarian class inherits from the base staff class
this is a for vet who performs health checks on animal
"""
class Veterinarian(Staff):
    def __init__(self, name):
        super().__init__(name, "Veterinarian")

    def conduct_checkup(self, animal, description, severity, treatment, date_reported):
        """
        method will perform health checks on animal and create a health record if none found 
        it will store the description, severity, treatment and date_reported for each animal 
        """
        recordings = HealthRecord(description, severity, treatment, date_reported)
        return f"{self.get_name()} Recorded: {recordings}"
