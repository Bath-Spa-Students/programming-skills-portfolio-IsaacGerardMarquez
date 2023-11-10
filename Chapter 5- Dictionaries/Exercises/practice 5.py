# Practice 5: Write a Python program to merge two dictionaries into one.

# I created a dictionary named "Isaac_Introduction" that stores information about myself.
Isaac_Introduction = {
    'Name': 'Isaac Gerard S. Marquez',
    'Nationality': 'Filipino',
    'Languages Spoken': ['English', 'Filipino', 'Hiligaynon'],
    'Age': 18,
    'Date of Birth' : 'January 25, 2005',
    'Sex': 'Male',
    'Address': "Al Qulaya'ah, Sharjah",
    'Contact Number': '971566630388',
    'Email Address': 'IsaacBathSpa@gmail.com',
    'Hobbies': ['Playing guitar', 'singing', 'cooking', 'photography', 'playing sports such as basketball and volleyball', 'learning'],
    'Pet': 'Maltipoo',
    'University': 'Bath Spa University RAK',
    'Current Level': 'Level 4 (Year 1)',
}

# I created another dictionary named "Additional_Information" that stores additional information about myself.
Additional_Information = {
    'Favorite Food': 'Adobo',
    'Favorite Drink': 'Milk',
    'Favorite Colors': 'Navy Blue and Maroon',
}

# Use "update()" to merge the two dictionaries into one. "update()" adds the key and value pairs from Additional_Information into Isaac_Introduction which modifies it in place.
Isaac_Introduction.update(Additional_Information)

# Use print() function to print or display the updated value of Isaac_Introduction.
print (Isaac_Introduction)