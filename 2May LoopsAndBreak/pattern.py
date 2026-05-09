'''5. Digit Alternating Sum System

A coding system calculates alternating sum of digits (add, subtract, add...).

Write a program to:

Traverse digits from left to right
Add first digit, subtract second, add third, and so on
Display final alternating sum
If result is positive → print Positive Pattern
Else → print Negative Pattern

Input:
1234

Output:
Result = -2
Negative Pattern

Input:
8642

Output:
Result = 8
Positive Pattern'''

'''num = input("ENTER NUMBER: ")

result = 0
add = True

for ch in num:
    digit = int(ch)

    if add:
        result += digit
    else:
        result -= digit

    add = not add

print("Result =", result)

if result > 0:
    print("Positive Pattern")
else:
    print("Negative Pattern")'''

#USING WHILE LOOP

num = int(input("Enter number: "))

temp = num
digits = 0

while temp > 0:
    digits += 1
    temp //= 10

result = 0

while num > 0:
    digit = num % 10

    if digits % 2 != 0:
        result += digit
    else:
        result -= digit

    digits -= 1
    num //= 10

print("Result =", result)

if result > 0:
    print("Positive Pattern")
else:
    print("Negative Pattern")

