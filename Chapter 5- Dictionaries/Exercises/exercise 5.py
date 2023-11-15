# Exercise 5: Pets (Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet)

# Creating an empty list named "pets" that would store multiple dictionaries, each representing a pet.
pets = []

pet = { # Store information to each pet in the list.
    'Kind of Animal (Species)': 'Dog',
    'Breed': 'Maltipoo',
    'Name': 'Coffee',
    'Age': '4 Months Old',
    'Gender': 'Male',
    'Owner': 'Isaac',
}
pets.append(pet) # The pets.append(pet) line is used to add each pet dictionary to the list named "pets", which can be accessed and printed later using a for loop.

pet = { # Store information to each pet in the list.
    'Kind of Animal (Species)': 'Cat',
    'Breed': 'Minuet',
    'Name': 'Toffee',
    'Age': '4 Months Old',
    'Gender': 'Female',
    'Owner': 'Khyle',
}
pets.append(pet) # The pets.append(pet) line is used to add each pet dictionary to the list named "pets", which can be accessed and printed later using a for loop.

pet = { # Store information to each pet in the list.
    'Kind of Animal (Species)': 'Turtle',
    'Breed': 'Red-eared slider',
    'Name': 'Ajina',
    'Age': '6 Months Old',
    'Gender': 'Male',
    'Owner': 'Radjn',
}
pets.append(pet) # The pets.append(pet) line is used to add each pet dictionary to the list named "pets", which can be accessed and printed later using a for loop.

# Displaying or printing the information that was stored about each pet.
for pet in pets:
    print(f"\nEverything that I know about {pet['Name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")