pets = []

pet = {
    'animal type': 'cat',
    'name': 'luna',
    'owner': 'basil',
    'weight': 30,
    'eats': 'fish',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'rachel',
    'owner': 'ahmed',
    'weight': 50,
    'eats': 'meat',
}
pets.append(pet)

pet = {
    'animal type': 'hamster',
    'name': 'Hamtaro',
    'owner': 'abdullah',
    'weight': 10,
    'eats': 'seeds',
}
pets.append(pet)

for pet in pets:
    print("\nThis is what i know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))