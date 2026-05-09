'''7.
Adam Number Verification System – Question

A high-security digital system is designed to validate special mirrored numbers known as Adam Numbers before granting access to sensitive data.

When a user enters a numeric code, the system performs a dual verification process:

* It calculates the square of the entered number.
* It reverses the number and calculates the square of the reversed value.
* Finally, it checks whether both results are mirror images (reverses) of each other.

A number is called an Adam Number if:
The square of the number and the square of its reverse are reverses of each other.

Task:
Write a Python program to check whether a given number is an Adam Number or not.

Examples:

Input:
12
Output:
Adam Number

Input:
13
Output:
Not an Adam Number

Input:
11
Output:
Adam Number

Example:
12 → 12² = 144, reverse(12) = 21 → 21² = 441 → reverse of 144'''

n=int(input("Enter Number = " ))
square = n*n
rev = 0
while n>0:
    rem = n % 10         #12%10=2 , 1%10=1
    rev = rev*10+rem     #0*10+2 = 2 , 2*10+1 = 21
    n = n // 10          # 12//10 = 1 , 1//10=0

square2 = rev*rev

rev_sqr = 0
while square2>0:
     rem = square2% 10         
     rev_sqr = rev_sqr*10+rem     
     square2 = square2 // 10  
       
if square==rev_sqr:
    print("Adam Number")

else:
    print("Not an Adam Number")
      


