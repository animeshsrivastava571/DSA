def duplicate_elements(lst):

# Brute force way
    duplicate_lst = []
    for i in range(len(lst)):
        cnt=0
        for j in range (0,i+1):
            if lst[j] == lst[i]:
                cnt = cnt+1
                if (cnt==2) and (lst[i] not in duplicate_lst) :
                    duplicate_lst.append(lst[i])
    print(duplicate_lst)


lst = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
lst1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# duplicate_elements(lst)





def duplicate_elements_efficient(lst):

# Efficient way O(n) is the time complexity
    duplicate_lst = []
    unique_lst = []


    for i in lst:
        if i not in unique_lst:
            unique_lst.append(i)
        elif i not in duplicate_lst:
            duplicate_lst.append(i)

    print(duplicate_lst)


lst = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
lst1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
duplicate_elements_efficient(lst)


