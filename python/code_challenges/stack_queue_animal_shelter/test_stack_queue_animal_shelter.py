from stack_queue_animal_shelter import AnimalShelter

def test_empty():
    animal_shelter = AnimalShelter()
    actual = animal_shelter.front
    expected = None
    assert actual == expected

def test_enqueue_one():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue("cat")
    actual = animal_shelter.front.value
    expected = "cat"
    assert actual == expected


def test_enqueue_multi_cat():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue("cat")
    animal_shelter.enqueue("dog")
    animal_shelter.enqueue("cat")

    actual = animal_shelter.front.value
    expected = "cat"
    assert actual == expected


def test_enqueue_multi_dog():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue("dog")
    animal_shelter.enqueue("cat")
    animal_shelter.enqueue("dog")

    actual = animal_shelter.front.value
    expected = "dog"
    assert actual == expected


def test_dequeue_queue_empty():
    animal_shelter = AnimalShelter()
    actual=animal_shelter.dequeue("cat")
    expected = "no animals"
    assert actual == expected

def test_dequeue_valid_cat():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue("dog")
    animal_shelter.enqueue("cat")
    animal_shelter.enqueue("dog")

    actual = animal_shelter.dequeue("cat")
    expected = "cat"
    assert actual == expected

def test_dequeue_invalid_pref():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue("dog")
    animal_shelter.enqueue("cat")
    animal_shelter.enqueue("dog")

    actual = animal_shelter.dequeue("horse")
    expected = "none"
    assert actual == expected


def test_dequeue_invalid_dog():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue("cat")
    animal_shelter.enqueue("cat")
    animal_shelter.enqueue("cat")

    actual = animal_shelter.dequeue("dog")
    expected = "none"
    assert actual == expected
