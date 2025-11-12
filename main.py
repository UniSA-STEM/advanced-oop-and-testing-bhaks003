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

print("\n")

print("====== Showing the string conversion implementation. =============")
print(lion)
print(crow)
print(snake)

print("\n")

print("====== Testing the method of make_sound. ========")
print(lion.make_sound())
print(crow.make_sound())
print(snake.make_sound())

print("\n")

print("====== Testing the method of daily_care. ======")
print(lion.daily_care())
print(crow.daily_care())
print(snake.daily_care())

print("\n")

print("======== Setting Up the enclosures and including animals. ========== ")
woodland = Enclosure("Black Woodland", "Woodland", 3, "mammal")
aviary = Enclosure("Aviary", "Aviary", 4, "bird")
lagoons = Enclosure("Lagoon", "Lagoon", 5, "reptile")


print("\n")

print("========== showing the string conversion implementation. =======")
print(woodland)
print(aviary)
print(lagoons)
