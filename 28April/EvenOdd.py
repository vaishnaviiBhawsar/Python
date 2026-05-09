'''9.Even Odd Difference Prime System

A smart scanner counts even and odd digits.

Write a program to:

- Count even digits
- Count odd digits
- Find difference
- Check whether difference is Prime or Not

Input:
123456

Output:
Even Count = 3
Odd Count = 3
Difference = 0
Not Prime'''

n=int(input("Enter Number"))
even_count=0
odd_count=0


while n>0:

     digit= n%10 
   
     if digit % 2 == 0:
         even_count+=1

     else:
         odd_count+=1

     n=n//10
     
print("Even Count = ", even_count)

print("odd Count = ", odd_count)

difference=even_count-odd_count
print("Difference =" , difference)

#Prime check
x=0
if difference<=1:
    print("Not Prime")
   

else:
   x=0
   i=2
   while i < difference :
       if difference % i == 0:
         x=1
         break
       i=i+1

if x==0:
   print("Prime")
else:
   print("Not Prime")


