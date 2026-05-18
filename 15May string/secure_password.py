'''
5.
Advanced Password Security Checker

A cyber security company wants to verify whether employee passwords are highly secure before giving system access.

Conditions: Password must:

Start with an uppercase letter
End with a digit
Contain at least 2 digits
Contain at least 1 special character (@ # $ % & *)
Must not contain spaces
Length should be between 8 and 15 characters

Input: Enter password: Python@45

Output: Secure Password
'''

password=input("Enter password:")
upper = 0
count = 0
special= 0
space = 0
last=0

if len(password)>=8 and len(password)<=15 :

    if password[0]>='A' and password[0]<='Z':
         upper=1
    if password[-1].isdigit() : 
         last=1

    for ch in password:

        if ch>='0' and ch<='9':
            count+=1

        elif ch==" ":
            space=1

        elif ch in '@#$%&*':
            special=1
            

if upper==1 and last==1 and count>=2 and space==0 and special==1:
    print("Secure password")
else: 
    print("InSecure password")

















































            
        
              

    