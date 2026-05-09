'''
3.
Digit Neighbor Sum Analyzer

A system analyzes the relationship between a digit and its immediate neighbors.

Write a program to:

Traverse digits from left to right (ignore first and last digit)
For each digit, calculate sum of its adjacent digits
Check if current digit is equal to the sum of its neighbors
Display such digits
Count how many such digits exist
If none found → print No Matching Digit
Else → print Neighbor Sum Pattern Found

Input:
121314

Output:
Matching Digits: 2 
Count = 1
Neighbor Sum Pattern Found'''

num = input("Enter Number: ")

count = 0

print("Matching Digits:",end=" ")

for i in range(1, len(num) - 1):
    left = int(num[i - 1])
    current = int(num[i])
    right = int(num[i + 1])

    if current == left + right:
        print(current, end=" ")
        count += 1

print("\nCount =", count)

if count>0:
    print(" Neighbor Sum Pattern Found")
else:
    print("No Matching Digit")
    



       