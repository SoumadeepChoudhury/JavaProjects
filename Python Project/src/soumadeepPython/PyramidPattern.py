# Create pyramid Pattern

c = '*'
for i in range(1, 6):

    for j in range(5, i, -1):
        print(' ', end='')
    for j in range(1, i+1):

        print(c, end='')
    for j in range(1, i):
        print(c, end='')
    print()
