'''4. Prime Security Code Checker – Advanced

A high-security lab accepts only prime numbered access codes.

When a user enters a number, the software must:

- Check whether number is prime
- If prime, print next immediate prime number
- If not prime, print previous immediate prime number

Write a program using loops only.

Input:
29

Output:
Prime Number
Next Prime = 31'''

n=int(input("Enter a number: "))

x=0
if n<=1:
   print("Not prime ")
i=2
while i<n:
   if n%i==0:
       x=1
       break
   i=i+1
   
if x==0:
    print("Prime Number")
    temp=n
    while True:
        temp=temp+1
        if temp<=1:
            continue
        else:
            i=2
            x=0
            while i<=temp//2:
                if temp%i==0:
                    x=1
                i=i+1
            if x==0:
                print("Next Prime =", temp)
                break

else:
    temp=n
    while True:
        temp=temp-1
        if n<=1:
            continue
        else:
            i=2
            x=0
            while i<=temp//2:
                if temp%i==0:
                    x=1
                i=i+1
            if x==0:
                print("Previous Prime =", temp)
                break



