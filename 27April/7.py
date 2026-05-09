'''7. Duck Number Checker

A verification system is used by an e-commerce company to validate promotional coupon numbers. Coupon numbers containing at least one zero in between digits are considered special duck numbers. However, if the number starts with zero, it is rejected immediately.

A duck number is a number that contains at least one zero but does not start with zero.

Example:
1023

Write a program using loops to check whether the entered number is a Duck number.

Input:
1023

Output:
Duck Number'''

n = int(input("Enter number: "))

temp = n
zero_count = 0

# check if number is zero (invalid start case)
if n == 0:
    print("Not Duck Number")
else:
    while temp > 0:
        digit = temp % 10

        if digit == 0:
            zero_count = zero_count + 1

        temp = temp // 10

    if zero_count > 0:
        print("Duck Number")
    else:
        print("Not Duck Number")
