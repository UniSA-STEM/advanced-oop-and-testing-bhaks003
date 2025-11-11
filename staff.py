'''
File: staff.py
Description: A brief description of this Python module.
Author: Krish Bhadani
ID: 110429045
Username: bhaks003
This is my own work as defined by the University's Academic Integrity Policy.
'''

from health_record import HealthRecord

class Staff:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def get_name(self):
        return self.name

    def get_role(self):
        return self.role
