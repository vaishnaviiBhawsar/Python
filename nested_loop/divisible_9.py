'''WAP to find out the sum of all integer between 100 and 200 which are divisible by 9'''

x = int(input("Enter first number"))
y = int(input("Enter second number"))



for num in range(x,y+1):
    sum = 0
   
    i = x
    while i<=num:
        if i % 9 == 0:
           sum = sum+i
     
        i = i+1

print("sum of digits which is divisible by 9 =" ,sum)