# Exercise 5: Cities (Write a function called describe_city() that accepts the name of a city and its country.)
# The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the default country.

# Function that would print three different cities, saying which country they are located in.

# The function named "describe_city" takes two arguments, which are City and Country. 
# The argument named "City" is a string that represents the name of a city, and the argument named "Country" is a string that represents the name of a country.
def describe_city(City, Country="Philippines"):

# Creating a message using string formatting and then using a print() function to display it.
    Message = f"{City.title()} city is located in the {Country.title()}."
    print(Message)

# The function creates and prints a message that states "Bacolod city is located in the Philippines.".
describe_city("Bacolod")

# The function creates and prints a message that states "Cebu city is located in the Philippines.".
describe_city("Cebu")

# The function creates and prints a message that states "Nassau city is located in the Bahamas.".
describe_city("Nassau", "Bahamas")