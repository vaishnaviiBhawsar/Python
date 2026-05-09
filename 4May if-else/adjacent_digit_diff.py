'''1. Adjacent Digit Difference Analyzer

A system analyzes differences between consecutive digits in a number.

Write a program to:

Find the difference between every pair of adjacent digits
Display all differences
Count how many differences are even
Find the largest difference
If all differences are same → print Uniform Difference
Else → print Non-Uniform Pattern

Input:
84261

Output:
Differences: 4 2 4 5
Even Differences Count = 3
Max Difference = 5
Non-Uniform Pattern'''

num = input("Enter Number: ")

count = 0
max_diff = 0  

print("Differences:")

for i in range(len(num)-1):
            
    diff = abs(int(num [i]) - int(num[i+1]))     
    print(diff,end=" ")

    if diff%2==0:
        count=count+1

    if diff > max_diff:   
        max_diff = diff

print("\nEven Differences Count = ",count)
print("Max Difference =",max_diff)

if diffrences == diffrences :
    print("Uniform Difference")
else:
    print("Non-Uniform Difference")