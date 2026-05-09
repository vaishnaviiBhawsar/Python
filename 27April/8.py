'''8.
Mirror Difference Transaction Verification System
A multinational banking company processes thousands of daily transaction IDs. To detect suspicious patterns and validate system-generated IDs,
 the security software performs a Mirror Difference Verification Test.
For every entered transaction ID:

Reverse the digits of the transaction ID

Find the absolute difference between the original ID and the reversed ID


Count the total number of digits in the difference


Apply the following conditions using if-elif-else:

If the difference is 0, print Perfect Match


Else if the difference is divisible by 9, print Verified


Else print Rejected


Write a program to automate this verification process using loops and conditional statements.
Input:
4215
Output:
Reverse = 5124Difference = 909Digits = 3Verified
Input:
1221
Output:
Reverse = 1221Difference = 0Digits = 1Perfect Match
Input:
1234
Output:
Reverse = 4321Difference = 3087Digits = 4Verified
'''

n=int(input("Enter the transaction id :"))
original=n
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10   
#print("Reverse = ",rev) 

diff=abs(rev-original)
count=0
diff1=diff

while diff>0:
    rem1=diff%10
    count+=1
    diff=diff//10
#print("difference digit count = ",count)

if diff1==0:
   print("Reverse = ",rev, "Differece = ",diff1, "Digit = ",count, "Perfect match")
elif diff1%9==0:
   print("Reverse = ",rev, "Differece = ", diff1, "Digit = ",count, "Verified")
else:
    print("rejected")