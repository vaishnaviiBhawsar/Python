'''5. Next Prime ID Generator – Smart Version

A company gives prime numbered employee IDs to premium staff.

Manager enters current ID.
System must:

- Find next prime number after current ID
- Find difference between current ID and next prime

Write a program using loops.

Input:
20

Output:
Next Prime ID = 23
Gap = 3'''

n=int(input("Enter a number: "))
temp=n
while True:
    n=n+1
    if n<=1:
        continue
    else:
        i=2
        x=0
        while i<=n//2:
            if n%i==0:
               x=1
            i=i+1
        if x==0:
           print("next prime number ",n)
           break

diff=n-temp
print("Gap",diff)