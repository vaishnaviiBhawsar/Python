'''
2.
Space Counter in Chat Messages

A chat application wants to calculate how many spaces are used in a message.

Input: Enter chat message: Good morning everyone how are you

Output: Total spaces: 5'''


msg=input("Enter chat message:")

space = 0
i = 0

while i<len(msg):
    ch=msg[i]
    if ch==" ":
        space=space+1
    i=i+1
    
print("Total spaces:",space)