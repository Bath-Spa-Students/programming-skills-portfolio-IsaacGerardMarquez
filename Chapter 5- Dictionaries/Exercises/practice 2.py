# Practice 2: Write a Python program to iterate through the keys of a dictionary and print them.

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

# Use for loop to iterate through the keys of the dictionary named "Isaac_Introduction".
for key in Isaac_Introduction:

# Use print() function to print or display each "key" on a separate line.
    print(key)