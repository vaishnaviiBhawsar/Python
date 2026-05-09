'''4.
1. Digit Gap Consistency Checker

A number analysis system checks whether the gap between digits follows a consistent pattern.

Write a program to:

Find the absolute difference between first two digits
Compare this difference with all next adjacent digit differences
If any difference is not equal to the first difference, stop using break
Display:
- Initial gap
- Whether all gaps are same or not

Input:
8642

Output:
Initial Gap = 2
Consistent Pattern

Input:
97531

Output:
Initial Gap = 2
Consistent Pattern

Input:
5321

Output:
Initial Gap = 2
Pattern Break Detected'''

'''num = input("Enter number: ")

prev = None
initial_gap = None

for ch in num:
    digit = int(ch)

    if prev is None:
        prev = digit
        continue

    gap = abs(prev - digit)

    if initial_gap is None:
        initial_gap = gap
        print("Initial Gap =", initial_gap)
    else:
        if gap != initial_gap:
            print("Pattern Break Detected")
            break

    prev = digit

else:
    print("Consistent Pattern")'''


#USING WHILE LOOP

num = int(input("Enter Number"))

prev = num % 10        # last digit
num = num // 10

curr = num % 10       # second last digit

initial_gap = abs(curr - prev)

print("Initial Gap =", initial_gap)

pattern_break = False

while num > 0:
    next_digit = num % 10

    gap = abs(next_digit - curr)

    if gap != initial_gap:
        pattern_break = True
        break

    curr = next_digit
    num = num // 10

if pattern_break:
    print("Pattern Break Detected")
else:
    print("Consistent Pattern")

