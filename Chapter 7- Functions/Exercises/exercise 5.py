# Exercise 5: Cities (Write a function called describe_city() that accepts the name of a city and its country.)
# The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the default country.

# Function that would print three different cities, saying which country they are located in.
def describe_city(City, Country="Philippines"):
    """Describing a city and in which country it is located."""
    Message = f"{City.title()} city is located in the {Country.title()}."
    print(Message)

describe_city("Bacolod")
describe_city("Cebu")
describe_city("Nassau", "Bahamas")