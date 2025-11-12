'''
File: health_record.py
Description: A brief description of this Python module.
Author: Krish Bhadani
ID: 110429045
Username: bhaks003
This is my own work as defined by the University's Academic Integrity Policy.
'''

class HealthRecord:
    """
    this health record class represent a single medical or health incdent of an animal
    it will stores information such as description, severity, treatment, date_reported and resolution status
    it will also track animal's ongoing and past health conditions.
    """
    def __init__(self, description, severity, treatment, date_reported):
        # using execption handling to make sure user is entering right data
        if not description:
            raise ValueError("Health issue description cannot be empty")
        if severity not in ["low", "moderate", "high", "serious"]:
            raise ValueError("Severity must be one only which is low, moderate, high, serious")
        if date_reported.count("/") != 2:
            raise ValueError("Date must be entered in the format DD/MM/YY.")

        self.__description = description
        self.__severity = severity
        self.__treatment = treatment
        self.__date_reported = date_reported
        self.__active = True
        self.__resolution_notes = ''

    def is_serious(self):  #determine the serious of an animal condition if it is serious or high it will return true value and false otherwise
        if self.__active and (self.__severity == "serious" or self.__severity == "high"):
            return True
        return False

    """
    this method will mark the current issue as resolved    
    """
    def mark_resolved(self, notes=""):
        self.__active = False
        self.__resolution_notes = notes


    # string conversion method
    # this will display the output in a readable manner
    def __str__(self):
        status = "active"
        if not self.__active:
            status = "Treated"
        text_display =  status + ":" + self.__description + " (" + self.__severity + ")" + self.__date_reported
        if self.__resolution_notes:
            text_display += f" | Notes: {self.__resolution_notes}"
        return text_display

