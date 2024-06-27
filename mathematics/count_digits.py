def count_digits(n):
    cnt =0
    while n!=0:
        dig = n%10
        cnt = cnt+1
        n = int(n/10) # yaha pe int pe typecast krna is important
        #print(cnt)
    return cnt

result1 = count_digits(9856000000009)
print(result1)

## Method 2 using // operator 

def count_digits_new(n):
    cnt =0
    while n!=0:
        n = n//10 # ///operator gives you to the quotient directly
        cnt = cnt+1
        #print(cnt)
    return cnt

result2= count_digits_new(9856000000009)
print(result2)