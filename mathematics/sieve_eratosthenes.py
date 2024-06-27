def sieve(n):
    " this function is used to print all prime numbers less than equal to n"

    prime_list = []
    final_list=[]

    for i in range(2,n+1):
        if i not in prime_list:
            final_list.append(i)
        
            for j in range(i*i,n+1,i):
                prime_list.append(j)
    return final_list

print(sieve(10))