def second_largest(lst): # this solution is O(n)

    max1=lst[0]
    second_max = lst[1]

    for element in lst:
        if element>max1:
            second_max = max1
            max1 = element
        elif element<max1 and element>second_max:
            second_max = element

    return max1,second_max


lst = [10,20,4,5,50,60,45,55]
a,b=second_largest(lst)

print(a)
print(b)