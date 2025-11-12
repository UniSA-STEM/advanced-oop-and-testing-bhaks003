'''
File: test_zoo_system.py
Description: Pytest unit tests for Zoo Management System.
Author: Krish Bhadani
ID: 110429045
Username: bhaks003
This is my own work as defined by the University's Academic Integrity Policy.
'''

import pytest
from mammal import Mammal
from bird import Bird
from reptile import Reptile
from enclosure import Enclosure
from zookeeper import Zookeeper
from veterinarian import Veterinarian


@pytest.fixture
def setup_zoo():
    """this type of fixutre will setup the most imp part in order to verify even classes as well."""
    lion = Mammal("Lion", "Simba", 21, "Meat")
    crow = Bird("Crow", "Kallu", 2, "Seed")
    snake = Reptile("Snake", "Nagin", 6, "Rat")

    woodland = Enclosure("Black Woodland", "Woodland", 3, "mammal")
    aviary = Enclosure("Aviary", "Aviary", 4, "bird")
    lagoon = Enclosure("Lagoon", "Lagoon", 5, "reptile")

    zookeeper = Zookeeper("Chachu", "Zookeeper")
    vet = Veterinarian("Dr. Chichu", "Veterinarian")

    return lion, crow, snake, woodland, aviary, lagoon, zookeeper, vet


# ---------- animal tests ----------
def animal_test_creation(setup_zoo):
    lion, crow, snake, *_ = setup_zoo
    assert lion.get_name() == "Simba"
    assert crow.get_species() == "Crow"
    assert snake.get_diet() == "Rat"


def testing_sound_care_animal(setup_zoo):
    lion, crow, snake, *_ = setup_zoo
    for animal in [lion, crow, snake]:
        assert isinstance(animal.make_sound(), str)
        assert isinstance(animal.daily_care(), str)
        assert len(animal.make_sound()) > 0


# ---------- enclosure tests ----------
def test_to_add_correct_animal(setup_zoo):
    lion, crow, snake, woodland, aviary, lagoon, *_ = setup_zoo

    woodland.add_animal(lion)
    aviary.add_animal(crow)
    lagoon.add_animal(snake)

    assert woodland.get_animal_count() == 1
    assert aviary.get_animal_count() == 1
    assert lagoon.get_animal_count() == 1


def test_to_add_wrong_species(setup_zoo):
    lion, crow, snake, woodland, aviary, lagoon, *_ = setup_zoo
    with pytest.raises(ValueError):
        aviary.add_animal(snake)
    with pytest.raises(ValueError):
        lagoon.add_animal(lion)


def test_to_remove_animal(setup_zoo):
    lion, _, _, woodland, *_ = setup_zoo
    woodland.add_animal(lion)
    msg = woodland.remove_animal("Simba")
    assert "removed" in msg or "not found" in msg


def test_cleaning_enclosure(setup_zoo):
    _, _, _, woodland, _, _, zookeeper, _ = setup_zoo
    if hasattr(woodland, "make_dirty"):
        woodland.make_dirty()
    result = zookeeper.clean_enclosure(woodland)
    assert "cleaned" in result
    assert woodland.get_cleanliness_level() == "Clean"


# ---------- veterinarian tests ----------
def test_vet_creating_health_record(setup_zoo):
    lion, *_ , vet = setup_zoo
    before = len(lion.get_health_summary())
    vet.conduct_checkup(lion, "Gastro infection", "serious", "Operate and rest", "13/11/25")
    after = len(lion.get_health_summary())
    assert after > before
    assert any("Gastro infection" in str(r) for r in lion.get_health_summary())
