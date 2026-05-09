'''
4.Digit Gap Analyzer

A system analyzes the gap between consecutive digits.

Write a program to:

Traverse digits from left to right
Find the absolute difference between current digit and next digit
Display each difference
Count how many differences are greater than 2
Find the maximum difference
If all differences ≤ 2 → print Smooth Number
Else → print Irregular Pattern

Input:
86421

Output:
Differences: 2 2 2 1
Count (>2) = 0
Max Difference = 2
Smooth Number'''


num = input("Enter Number :")
count = 0
max_diff = 0

print("Differences:")

for i in range (0 ,len(num)-1):
      diff = abs(int(num[i])-int(num[i + 1]))
      print(diff, end=" ")

      if diff >2:
         count=count+1

      if diff > max_diff:
          max_diff = diff
    

print("\nCount(>2) =" ,count)
print("Max Diffrence = " ,max_diff)
 
if diff<=2:
    print("Smooth Number")
else:
    print("Irregular Pattern")