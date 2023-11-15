# Exercise 3: Glossary 2 (Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.)

# Creating a dictionary named "My_Glossary" that would store 10 Python programming words that I have learned about in the previous chapters.
My_Glossary = {
    "Variable": " A name that represents a value stored in the computer's memory.",
    "Function": " A group of statements within a program that perform as specific task.",
    "String": " A data type that is inside single or double quotations which is composed of a collection of characters which can include letters and numbers.",
    "String Concatenation": " Adding or joining two or more strings to create a single new string.",
    "Comments": " Notes of explanation that document lines or sections of a program which are identified with a hash symbol (#).",
    "Boolean": " A data type that only has two possible values: True or False.",
    "Pseudocode": " A simplified language that is a bit closer to a programming language.",
    "Lists": " Used to store a collection of multiple values in a single variable.",
    "Bugs": " Errors in code.",
    "Indentation":  " The spaces at the beginning of a code line",
    }

# Using for Loop that would run through the dictionary’s keys and values
for Word, Definition in My_Glossary.items():
    print ("\n" + Word.title() + ":" + Definition)