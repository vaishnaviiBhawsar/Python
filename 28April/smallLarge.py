'''
8. Largest Smallest Sum Prime Checker

A number analyzer finds largest and smallest digit.

Write a program to:

- Find largest digit
- Find smallest digit
- Find sum of both
- Check whether sum is Prime or Not

Input:
57294

Output:
Largest = 9
Smallest = 2
Sum = 11
Prime '''

n = int(input("Enter number: "))

temp = n
largest = 0
smallest = 9

# Find largest and smallest digit
while temp > 0:
    digit = temp % 10
    
    if digit > largest:
        largest = digit
    if digit < smallest:
        smallest = digit
    
    temp //= 10

total = largest + smallest

# Prime check using x
x = 1

if total <= 1:
    x = 0
else:
    i = 2
    while i * i <= total:
        if total % i == 0:
            x = 0
            break
        i += 1

# Output
print("Largest =", largest)
print("Smallest =", smallest)
print("Sum =", total)

if x == 1:
    print("Prime")
else:
    print("Not Prime")
