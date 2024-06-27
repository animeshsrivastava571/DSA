'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".




Example 1:

Input: strs = ["flower","flow","flight"]

Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]

Output: ""

Explanation: There is no common prefix among the input strings.

'''

lst_str = ["flower","flow","fliwght"]
lst_str = ["cat","flow","fliwght"]

def common_prefix(lst_str):
    temp = []
    pre =''
    max_len = 0
    for elem in lst_str:
        len_str = len(elem)
        if len_str>max_len:
            max_len = len_str
            str_max = elem
    

    temp1 = ''
    # print(str_max)


    for i in range(len(str_max)-1):
        pre =  pre + str_max[i]
        #print(pre)

        for elem1 in lst_str:
            if elem1.startswith(pre):
                if str_max[i] not in temp:
                    temp.append(str_max[i])
                    temp1 = ''.join(temp)
                
            else:
                if temp1=='':
                    return ""
                else:
                    return temp1
        
    
print(common_prefix(lst_str))       
    