def palindrome(n):
    rev = 0
    temp = n
    while n!=0:
        dig = n%10
        rev = rev*10 + dig
        n = n//10
    
    if rev == temp:
        return ("Palindrome")
    else:
        return ("Not Palindrome")

print(palindrome(122))