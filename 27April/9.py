'''[1:06 PM, 4/27/2026] +91 88210 14212: 9.
Step Difference Number Analyzer

A mathematics research center studies hidden patterns inside numbers.
For every entered number, the system compares adjacent digits step by step.

Write a program to:

Find the absolute difference between every pair of adjacent digits
Display all step differences
Find the sum of all step differences
Find the largest step difference
If the sum of step differences is divisible by the number of digits, print Balanced Number
Otherwise print Unbalanced Number

Use loops wherever required.

Input:
57294
Output:
Step Differences: 2 5 7 5
Sum = 19
Largest = 7
Unbalanced Number'''

n = int(input("Enter number: "))

# Step 1: extract digits (in reverse order)
digits = []

temp = n
while temp > 0:
    digits.append(temp % 10)
    temp = temp // 10

# Step 2: reverse digits to get correct order
i = 0
j = len(digits) - 1
while i < j:
    digits[i], digits[j] = digits[j], digits[i]
    i += 1
    j -= 1

# Step 3: compute step differences
sum_diff = 0
max_diff = 0

print("Step Differences:", end=" ")

i = 0
count_digits = len(digits)

while i < count_digits - 1:
    diff = digits[i] - digits[i + 1]

    if diff < 0:
        diff = -diff  # absolute value using loop logic

    print(diff, end=" ")

    sum_diff = sum_diff + diff

    if diff > max_diff:
        max_diff = diff

    i += 1

print("\nSum =", sum_diff)
print("Largest =", max_diff)

# Step 4: Balanced / Unbalanced check
if sum_diff % count_digits == 0:
    print("Balanced Number")
else:
    print("Unbalanced Number")



