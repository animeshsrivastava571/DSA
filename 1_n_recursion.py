def fun(n):
    if n <1:
        return 
    else:
        fun(n-1)
        print(n)

fun(5)