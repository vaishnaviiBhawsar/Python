'''*9. Check All Digits Are Even*
A machine only accepts numbers where every digit is even. If any digit is odd, the number is rejected.
Write a program to *check whether all digits of a number are even using loops*.

Input: 2468
Output: All Even

Input: 2456
Output: Not All Even'''

num=int(input("Enter Number:"))
count = 0

while num > 0:
 num = num % 10 

if num % 2 == 0: 
      print("All Even")
else:
       print("Not All Even")


