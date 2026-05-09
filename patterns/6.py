'''6)
a
ab
abc
abcd
abcde'''

n =int(input("Enter number: "))
i =1
while i<=n:
    print()
    j = 1
    ch = 97
    while j<=i:
        print(chr(ch),end=" ")
        ch = ch+1
        j = j+1
    i= i+1
   
