def check_list_sorted(lst):
    flag = 0
    for i in range(len(lst)-2):
        if lst[i+1] - lst[i] >= 0 and lst[i+2]-lst[i+1] >=0:
            flag=1
        elif lst[i+1] - lst[i] <= 0 and lst[i+2]-lst[i+1] <=0:
            flag =1
        else:
            flag =0
            break
    
    if flag ==1:
        print('Sorted')
    elif flag ==0:
        print("Unsorted")

lst = [9, 4, 5, 8, 10]
lst1= [1, 4, 4, 8, 10]
check_list_sorted(lst)