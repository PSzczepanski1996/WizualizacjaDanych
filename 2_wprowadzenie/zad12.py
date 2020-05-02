for x in range(0, 11):
    for y in range(0, 11):
        print(str(x * y).rjust(3, ' '), end=' ')
    print()