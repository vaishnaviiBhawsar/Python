'''4.
Armstrong Number Finder

A digital number analysis system checks for Armstrong numbers within a range.
The user enters starting and ending numbers.
The system finds all Armstrong numbers using nested loops.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Armstrong Numbers are:
1
153
370
371
407'''

'''x=int(input("Enter starting number:"))
y=int(input("Enter ending number:"))

for i in range(x,y+1):
    temp = 0 
    power = len(str(i))
    total = 0
    while temp>0:
        rem = temp % 10
        total = total + rem ** power
        temp = temp // 10
        
    if total == n:
        print(n)'''

x=int(input("Enter starting number:"))
y=int(input("Enter ending number:"))

print("Armstrong Numbers are:")

for num in range(x,y+1):
    temp = num
    t=len(str(num))
    sum = 0

    while temp>0:
        rem = temp % 10
        sum = sum+rem**t
        temp = temp // 10

    if sum==num:
        print(num)