def second_largest(lst):

    unique_list = []
    
    for i in lst:
        if i not in unique_list:
            unique_list.append(i)

    max_element = max(unique_list)
    lst.remove(max_element)

    second_max_element = max(lst)

    print(second_max_element)

lst = [10,9,8,10,11,12,7,-20]

second_largest(lst)
