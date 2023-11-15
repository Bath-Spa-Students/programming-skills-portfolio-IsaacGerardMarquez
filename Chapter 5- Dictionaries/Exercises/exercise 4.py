#Exercise 4: Rivers (Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.)
#Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
#Use a loop to print the name of each river included in the dictionary
#Use a loop to print the name of each country included in the dictionary.

# Creating a dictionary named "Major_Rivers" that contains three major rivers and the countries they each run through.
Major_Rivers = {
    "Cagayan" : "Philippines",
    "Volga": "Russia",
    "Missouri": 'United States of America',
    }

# Creating a loop that prints (the river) runs through (the country).
for river, Country in Major_Rivers.items():
    print(f"The {river.title()} runs through {Country.title()}.")

# Creating a loop that prints the name of each river included in the dictionary.
print("\nThe following rivers are included in this data set:")
for river in Major_Rivers.keys():
    print(f"- {river.title()}")

# Creating a loop that prints the name of each country included in the dictionary.
print("\nThe following countries are included in this data set:")
for Country in Major_Rivers.values():
    print(f"- {Country.title()}")