'''
1
23
456
78910

'''
n = int(input("Enter number:"))

i=1
k = 1
while i<=n:
    print()
    j =1
    while j<=i:
        print(k , end=" ")
        j = j+1
        k = k+1
    i = i+1
    