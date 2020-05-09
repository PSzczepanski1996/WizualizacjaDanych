A = [1/x for x in range(1, 11)]
B = [x*x for x in range(1, 11)]
print(A)
print(B)
C = [x for x in B if not x//4]
print(C)