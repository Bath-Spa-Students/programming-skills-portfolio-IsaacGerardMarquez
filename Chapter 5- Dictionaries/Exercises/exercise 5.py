# Exercise 5: Pets (Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet)

# An empty list to store the "pets" in.
pets = []

# Store information to each pet in the list.
pet = {
    'Kind of Animal (Species)': 'Dog',
    'Breed': 'Maltipoo',
    'Name': 'Coffee',
    'Age': '4 Months Old',
    'Gender': 'Male',
    'Owner': 'Isaac',
}
pets.append(pet)

pet = {
    'Kind of Animal (Species)': 'Cat',
    'Breed': 'Minuet',
    'Name': 'Toffee',
    'Age': '4 Months Old',
    'Gender': 'Female',
    'Owner': 'Khyle',
}
pets.append(pet)

pet = {
    'Kind of Animal (Species)': 'Turtle',
    'Breed': 'Red-eared slider',
    'Name': 'Ajina',
    'Age': '6 Months Old',
    'Gender': 'Male',
    'Owner': 'Radjn',
}
pets.append(pet)

# Display or printing the information that was stored about each pet.
for pet in pets:
    print(f"\nEverything that I know about {pet['Name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")