'''2.
Digit Order Break Analyzer

A number validation system checks whether digits of an ID follow a strict increasing pattern. The moment the pattern breaks, the system stops further checking.

Write a program to:

Traverse the digits from left to right
Check whether each digit is greater than the previous digit
If the pattern breaks at any point, stop checking further using break
Display the position where the order breaks (1-based index)
If no break occurs, print Strictly Increasing Number

Use loops and break wherever required.

Input:
12357

Output:
Strictly Increasing Number

Input:
12342

Output:
Break at position = 4
Not Increasing Number'''

number = input("Enter Number:")


i = 1
while i <len(number):
    prev = int(number[i-1])
    curr = int(number[i])

    if curr <= prev:
         print("Order breaks at position =",i+1)
         break

    i = i+1
else:
    print("Digits are stricttly increasing ")    

