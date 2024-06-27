'''
Example 1:
Input: takeUforward
Output: a
Explanation: Character a is the left-most repeating character or the first repeating character.

Example 2:

Input: programming
Output: r
Explanation: Character r is the left-most repeating character or the first repeating character.

'''


def lst_most_repeating(str1): # Most efficient way using Frequency Array method

    index_arr = [0]*255

    for i in range (len(str1)):
        index_arr[ord(str1[i])] = index_arr[ord(str1[i])]+1

    for i in range (len(str1)):
        if index_arr[ord(str1[i])] >1:
            return str1[i]
    
    return -1

print(lst_most_repeating("programming"))

        


    
