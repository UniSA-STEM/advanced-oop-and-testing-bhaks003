'''
File: main.py
Description: Demonstration of the Zoo Management System functionality.
Author: Krish Bhadani
ID: 110429045
Username: bhaks003
This is my own work as defined by the University's Academic Integrity Policy.
'''

from mammal import Mammal
from bird import Bird
from reptile import Reptile
from health_record import HealthRecord
from zookeeper import Zookeeper
from veterinarian import Veterinarian
from enclosure import Enclosure


"in this section we will create the animals based on the category"

print("===== Creating Animals =====")
lion = Mammal("Lion", "Simba", 21, "Meat")
crow = Bird("Crow", "Kallu", 2, "Seed")
snake = Reptile("Snake", "Nagin", 6, "Rat")

print("\n=== Showing the string conversion implementation ===")
print(lion)
print(crow)
print(snake)

# testing the output of the animals making the sound
print("\n=== Testing make_sound() method ===")
print(lion.make_sound())
print(crow.make_sound())
print(snake.make_sound())

# testing daily care method
print("\n=== Testing daily_care() method ===")
print(lion.daily_care())
print(crow.daily_care())
print(snake.daily_care())

"""
assigning the encloure according the category of defined animals
"""
print("\n=== Setting Up Enclosures and Adding Animals ===")
woodland = Enclosure("Black Woodland", "Woodland", 3, "mammal")
aviary = Enclosure("Aviary", "Aviary", 4, "bird")
lagoons = Enclosure("Lagoon", "Lagoon", 5, "reptile")


woodland.add_animal(lion) #checking method works, by adding and removing the animals as well
aviary.add_animal(crow)
lagoons.add_animal(snake)
woodland.remove_animal("Simba")

# printing output of each enclosures to display animals in it
print("\n=== Checking Animals in Each Enclosure ===")
print(woodland)
print(woodland.list_animals())
print(aviary)
print(aviary.list_animals())
print(lagoons)
print(lagoons.list_animals())


"""
instantiating the staff member by the task 
"""
print("\n=== Creating Staff ===")
zookeeper = Zookeeper("Chachu")
veterinarian = Veterinarian("Dr. Chichu")
print(zookeeper)
print(veterinarian)

# in here each staff member will perfomr task
print("\n=== Staff Performing Tasks ===")
print(zookeeper.clean_enclosure(woodland))
print(zookeeper.feed_animal(lion))
print(veterinarian.conduct_checkup(lion, "Gastro infection", "serious", "Operate and rest", "13/11/25"))

"recording the health record and updating that as well"
print("\n=== Health Record Demonstration ===")
record = HealthRecord("Wing injury", "high", "Bandage and rest", "10/11/25")
print(record)
record.mark_resolved("Healed completely after 5 days.")
print(record)


#tracking on particular animal health record
print("\n=== Demonstrating Health Tracking for Animal Objects ===")
lion.add_health_issues("Fever", "moderate", "Antibiotics and rest", "13/11/25")
lion.add_health_issues("Fractured paw", "high", "Bandage and restricted movement", "14/11/25")

print(f"Does {lion.get_name()} have any serious active issues? {lion.has_serious_active_issues()}")

print(f"\nHealth Summary for {lion.get_name()}:")
for issue in lion.get_health_summary():
    print(issue)

print("\n=== Final System Status ===")
print(woodland)
print(aviary)
print(lagoons)
