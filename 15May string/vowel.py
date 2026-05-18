'''
1.Vowel Counter in Customer Feedback

 A company wants to analyze customer feedback messages by counting how many vowels are present in the feedback.

Input: Enter feedback message: Hello Customer Service

Output: Total vowels: 8'''


msg = input("Enter feedback message:")
i=0

vowel = 0


while i<len(msg):
    
    if msg[i] in "aeiou":
        vowel+=1

    i=i+1

print("Total vowels:",vowel)





          