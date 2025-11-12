'''
File: staff.py
Description: A brief description of this Python module.
Author: Krish Bhadani
ID: 110429045
Username: bhaks003
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Staff:
    """
    creating class staff which has attributes like name and role
    and with that using exception to raise error if invalid input given
    """
    def __init__(self, name, role):
        if not name:
            raise ValueError("Name cannot be empty")
        if not role:
            raise ValueError("Role cannot be empty")
        self.__name = name
        self.__role = role


    #using getters
    def get_name(self):
        return self.__name

    def get_role(self):
        return self.__role

    # string conversion method
    def __str__(self):
        return f"Staff: {self.__name} | Role: {self.__role}"


# staff_member = Staff("Alex", "Zookeeper")
# print(staff_member.get_name())
# print(staff_member.get_role())
# print(staff_member)