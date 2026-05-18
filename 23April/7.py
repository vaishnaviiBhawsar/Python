'''*7. Count Even Digits*
A data analyst is analyzing numeric IDs and needs to determine how many digits in the ID are even.
Write a program to *count the number of even digits in a given number using loops*.

Input: 123456
Output: Even digits count = 3'''


num = int(input("Enter a value of number:"))
count = 0

while num > 0:
    digit = num % 10   # get last digit

    if digit % 2 == 0: # check even
        count += 1

    num = num // 10    # remove last digit

print("Even digits count =", count)
