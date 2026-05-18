'''
12) Hollow Diamond Numbers
       1
      2 2
     3   3
    4     4
     3   3
      2 2
       1
'''
# 12) Hollow Diamond Numbers

n = 4

for i in range(1, n + 1):

    for space in range(n - i):
        print(" ", end="")

    print(i, end="")

    if i > 1:
        for space in range(2 * i - 3):
            print(" ", end="")
        print(i, end="")

    print()

for i in range(n - 1, 0, -1):

    for space in range(n - i):
        print(" ", end="")

    print(i, end="")

    if i > 1:
        for space in range(2 * i - 3):
            print(" ", end="")
        print(i, end="")

    print()