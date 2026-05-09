'''6.
Palindrome Number Range Checker

A barcode verification system checks for palindrome numbers within a specific range.
The user enters starting and ending numbers.
The system displays all palindrome numbers using nested loops.

Input:
Enter starting number: 100
Enter ending number: 200

Output:
Palindrome Numbers are:
101
111
121
131
141
151
161
171
181
191'''


x=int(input("Enter starting number:"))
y=int(input("Enter ending number:"))

print("Palindrome Numbers are:")

for num in range(x,y+1):
    rev = 0
    temp = num
    
    while temp>0:
        rem = temp % 10
      
        rev = rev*10+rem
        temp = temp // 10
    if rev == num:
         print(num)
        