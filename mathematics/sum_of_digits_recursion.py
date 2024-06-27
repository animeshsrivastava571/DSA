def sumofnumbers(n):
    if n==0:
        return 0
    else:
        return n + sumofnumbers(n-1)


print(sumofnumbers(3))