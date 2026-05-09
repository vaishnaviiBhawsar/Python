'''
4. Strong Number Checker

A digital lock opens only for strong numbers.

A strong number is a number whose sum of factorial of digits equals the number.

Example:
145 = 1! + 4! + 5!

Write a program using loops to check strong number.

Input:
145

Output:
Strong Number'''


n = int(input("Enter Number: "))
original = n
sum_fact = 0

while n > 0:
    digit = n % 10
    
    fact = 1
    i = 1
    while i <= digit:
        fact = fact * i
        i += 1

    sum_fact += fact
    n = n // 10

if sum_fact == original:
    print("Strong Number")
else:
    print("Not a Strong Number")

