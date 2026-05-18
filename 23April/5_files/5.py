'''5. Palindrome Check
A number plate is considered special if it reads the same forward and backward. Such numbers are called palindromes.
Write a program to *check whether a given number is a palindrome using loops*.

Input: 121
Output: Palindrome'''

n=int(input("Enter a Number: "))
temp=n
sum=0

while n>0:
    r=n%10
    sum=sum*10+r
    n=n//10

if temp==sum:
    print("Palindrome Number")
        
else: 
    print("Not Palindrome Number")