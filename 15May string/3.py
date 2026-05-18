'''

3.
Character Occurrence Checker in Product Review

An e-commerce website wants to know how many times a particular character appears in a product review.

Input: Enter product review: this product is really good
 Enter character to check: o

Output: Character 'o' occurs: 4 times
'''

n= input("Enter product review:")
i = 0
count=0
while i<len(n):
    ch=n[i]
    if ch=='o':
        count=count+1
    i=i+1
print("Character 'o' occurs:",count)
