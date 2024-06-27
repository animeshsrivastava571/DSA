def gcd(a,b):

    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a


print(gcd(12,16))



# to find lcm, use the formula: a*b= gcd * lcm