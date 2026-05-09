'''
4.Spy Number Detector

A cybersecurity system flags special numeric codes.

A number is called a Spy Number if:
Sum of digits = Product of digits

Write a program to check whether the entered number is Spy Number or Not.

Input:
1124

Output:
Spy Number'''

n = int(input("Enter Number = " ))
sum = 0 
mul = 1
temp = n
  
while n>0:
    rem= n % 10 
    sum = sum + rem 
    n = n // 10 

while temp>0:  
     rem= temp % 10 
     mul = mul * rem 
     temp = temp // 10 


if sum==mul :
    print("Spy Number")
else:
    print(" Not Spy Number")