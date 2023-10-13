#Exercise 3: Stripping Names (Tidy up the code to make it easier to understand Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, “\t” and “\n”, at least once. Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().)

Name = "\tIsaac Marquez\n"

print ("Unmodified:")
print (Name)

print ("\nUsing lstrip():")
print (Name.lstrip())

print ("\nUsing rstrip():")
print (Name.rstrip())

print ("\nUsing strip():")
print (Name.strip())