s = "cadbzabcd"

map = {}

left=0
max_len = 0

for right in range(len(s)):
    

    if s[right] not in map:
        map[s[right]] = right
        len_str = right - left +1

    elif s[right] in map and map[s[right]]>=left:
        left = map[s[right]] + 1 #update left
        map[s[right]] = right #update the map 
        len_str = right - left +1


    max_len = max(max_len,len_str)

print(max_len)

    