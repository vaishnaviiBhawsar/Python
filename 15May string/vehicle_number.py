'''7
.
Vehicle Number Plate Checker

The traffic department wants to validate vehicle registration numbers.

Conditions:
- First 2 characters should be alphabets
- Next 2 should be digits
- Total length should be 10

Input:
Enter vehicle number: MP04AB1234

Output:
Valid Vehicle Number'''


n = input("Enter vehicle number: ").lower()

if len(n) == 10:

    if n[0]>='a' and n[0]<='z' and n[1]>='a'and n[1]>='z':

        if n[2] >='0' and n[2]<='9' and n[3]>='0' and n[3]<='9':

            print("Valid Vehicle Number")

        else:
            print("Invalid Vehicle Number")

    else:
        print("Invalid Vehicle Number")

else:
    print("Invalid Vehicle Number")