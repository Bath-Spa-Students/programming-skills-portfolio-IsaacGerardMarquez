# Exercise 2: Glossary (A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.)
#Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
#Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

# Creating a dictionary named "My_Glossary" that would store Five (5) Python programming words that I have learned about in the previous chapters.
My_Glossary = {
    "Variable": "A name that represents a value stored in the computer's memory.",
    "Function": "A group of statements within a program that perform as specific task.",
    "String": "A data type that is inside single or double quotations which is composed of a collection of characters which can include letters and numbers.",
    "String Concatenation": "Adding or joining two or more strings to create a single new string.",
    "Comments": "Notes of explanation that document lines or sections of a program which are identified with a hash symbol (#).",
    }

# Print the words and their definitions.
Word = "Variable"
print(f"\n{Word.title()}: {My_Glossary[Word]}")

Word = "Function"
print(f"\n{Word.title()}: {My_Glossary[Word]}")

Word = "String"
print(f"\n{Word.title()}: {My_Glossary[Word]}")

Word = "String Concatenation"
print(f"\n{Word.title()}: {My_Glossary[Word]}")

Word = "Comments"
print(f"\n{Word.title()}: {My_Glossary[Word]}")