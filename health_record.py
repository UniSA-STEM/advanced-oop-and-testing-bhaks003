'''
File: health_record.py
Description: A brief description of this Python module.
Author: Krish Bhadani
ID: 110429045
Username: bhaks003
This is my own work as defined by the University's Academic Integrity Policy.
'''

class HealthRecord:
    def __init__(self, description, severity, treatment):
        if not description:
            raise ValueError("Health issue description cannot be empty")
        if severity not in ["low", "moderate", "high", "critical"]:
            raise ValueError("Severity must be one only which is low, moderate, high, critical")

        self.__description = description
        self.__severity = severity
        self.__treatment = treatment
        self.__active = True
        self.__resolution_notes = ''

