def rotate(lst):
    x = lst[0]

    for i in range(0,len(lst)-1):
        lst[i] = lst[i+1]

    lst[len(lst)-1] = x

    return lst

lst = [9, 4, 5, 8, 10]
lst1= [1, 4, 4, 8, 10]
print(rotate(lst1))