''' Prime Sum Lucky Number

A lottery app checks if sum of digits is prime.

Write a program to:

- Find sum of digits
- If prime print Lucky Number
- Else Normal Number

Input:
4528

Output:
Sum = 19
Lucky Number'''


n=int(input("Enter Number: "))
sum=0
while n>0:
    rem=n%10
    sum=sum+rem
    n=n//10
print("Sum =",sum)

i=2
x=0
while i<n:
   if n%i==0:
     x=1
     break
   i+=1

if x==0:
     print("Lucky Number ")
else:
     print("Normal Number")
    

