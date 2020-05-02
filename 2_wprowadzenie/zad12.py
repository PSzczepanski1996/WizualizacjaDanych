for x in range(1, 11):
    for y in range(1, 11):
        print(str(x * y).rjust(3, ' '), end=' ')
    print()