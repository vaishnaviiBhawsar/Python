'''
4.
Consonant Counter in Student Name Record

A school management system wants to count how many consonants are present in student names.

Input: Enter student name: Ajay Singh Thakur

Output: Total consonants: 11

NOTE:

Ignore case sensitivity (treat A and a same)
Consider only English alphabets for vowel/consonant counting
Vowels: A, E, I, O, U
'''

n = input("Enter student name: ").lower()

cons = 0

for i in range(len(n)):
    ch = n[i]

    if ch >= 'a' and ch <= 'z':
        if ch not in "aeiou":
            cons = cons + 1

print("Total consonants:", cons)