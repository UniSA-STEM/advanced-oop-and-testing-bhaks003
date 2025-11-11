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

class Veterinarian(Staff):
    def __init__(self, name):
        super().__init__(name, "Veterinarian")

    def conduct_checkup(self, animal, description, severity, treatment, date_reported):
        recordings = HealthRecord(description, severity, treatment, date_reported)
        return f"{self.get_name()} Recorded: {recordings}"
