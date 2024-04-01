def cons_ones(lst):
    cnt = 0
    max_cnt=0
    for i in range(len(lst)):
        if lst[i]==1:
            cnt = cnt+1
            if cnt>max_cnt:
                max_cnt=cnt
        elif lst[i] ==0:
            cnt=0
    print (max_cnt)


lst = [1, 1, 0, 1, 1, 1,0,0,1,1,1,1,1,1,0]
cons_ones(lst)
