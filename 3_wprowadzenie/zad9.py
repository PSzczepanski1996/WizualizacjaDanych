def iloczyn_ciagu(a1=1, r=1, ile=10):
    iloczyn = a1*r
    for x in range(r+1, ile+2):
        iloczyn += (x+r)*((x-1)*r)
    return iloczyn


print(iloczyn_ciagu())