'''
2. Digit Sum Mirror Checker
A validation system checks symmetry in digit sums.

Write a program to:

Split number into two halves
Find sum of first half digits
Find sum of second half digits
Display both sums
If both sums are equal → print Balanced Number
Else → print Unbalanced Number

Input:
123321

Output:
First Half Sum = 6
Second Half Sum = 6
Balanced Number'''

'''num = input("Enter number:")

mid = len(num) // 2

first_half = num[:mid]
second_half = num[mid:]

sum1 = 0
for digit in first_half:
    sum1+=int(digit)

print("First Half Sum =" , sum1)

sum2 = 0
for digit in second_half:
    sum2+=int(digit)

print("Second Half Sum =" , sum2)

if sum1==sum2:
    print("Balanced Number")
else:
    print("Unbalanced Number") '''

#USING WHILE LOOP

num = input("Enter Number: ")

mid = len(num) // 2

# first half sum
i = 0
sum1 = 0
while i < mid:
    sum1 += int(num[i])
    i += 1

# second half sum
i = mid
sum2 = 0
while i < len(num):
    sum2 += int(num[i])
    i += 1

print("First Half Sum =", sum1)
print("Second Half Sum =", sum2)

if sum1==sum2:
    print("Balanced Number")
else:
    print("Unbalanced Number") 


