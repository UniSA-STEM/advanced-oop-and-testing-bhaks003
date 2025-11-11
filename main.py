'''
File: main.py
Description: A brief description of this Python module.
Author: Krish Bhadani
ID: 110429045
Username: bhaks003
This is my own work as defined by the University's Academic Integrity Policy.
'''

from mammal import Mammal
from bird import Bird
from reptile import Reptile
from health_record import HealthRecord
from staff import Staff
from zookeeper import Zookeeper
from veterinarian import Veterinarian
from  enclosure import Enclosure


print(f"===== Creating Animals ====")
lion = Mammal("Lion", "Simba", 21, "Meat")
crow = Bird("Crow", "Kallu", 2, "Seed")
snake = Reptile("Snake", "Nagin", 6, "Rat")

