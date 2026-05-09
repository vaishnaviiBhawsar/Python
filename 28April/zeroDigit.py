'''10.Zero Count Prime Scanner

A banking system checks account numbers.

Write a program to:

- Count zero digits
- Find sum of digits
- Add zero count and sum
- Multiply by smallest digit
- Check whether final result is Prime or Not

Input:
908406

Output:
Zero Count = 2
Sum = 27
Smallest Digit = 0
Final Result = 0
Not Prime'''

 
n = int(input("Enter number: "))

temp = n

zero_count = 0
digit_sum = 0
smallest_digit = 9

    digit = temp % 10

    if digit == 0:
        zero_count += 1

    digit_sum += digit

    if digit < smallest_digit:
        smallest_digit = digit

    temp = temp // 10

# calculations
final_result = (zero_count + digit_sum) * smallest_digit

print("Zero Count =", zero_count)
print("Sum =", digit_sum)
print("Smallest Digit =", smallest_digit)
print("Final Result =", final_result)

# Prime check
if final_result <= 1:
    print("Not Prime")
else:
    i = 2
    x = 0

    while i < final_result:
        if final_result % i == 0:
            x = 1
            break
        i += 1

    if x== 0:
        print("Prime")
    else:
        print("Not Prime")
