'''
18) Binary Floyd Triangle
    1
    0 1
    1 0 1
    0 1 0 1
'''

n = int(input("Enter number of rows: "))

num = 1

for i in range(1, n + 1):

    for j in range(i):

        if num % 2 == 0:
            print(0, end=" ")
        else:
            print(1, end=" ")

        num += 1

    print()