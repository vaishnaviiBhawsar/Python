'''6.
Data Validation System – Character Identifier
A system needs to validate user input characters.
If the input is:
Alphabet → display "Alphabet"
Digit → display "Digit"
Otherwise → display "Special Character"
Write a program using inline if to classify the character.'''

char = input("Enter character: ")

print("Alphabet") if char.isalpha() else print("Digit") if char.isdigit() else print("Special Character")


#print("Alphabet")if str(char>='a') and str(char<='z')else print("Digit") if char>=0 and char<=9  else print("Special Character")











9