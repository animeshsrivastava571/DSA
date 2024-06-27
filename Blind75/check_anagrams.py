'''
Given two strings s1 and s2, check if both the strings are anagrams of each other.
Input : s1 = "listen"
        s2 = "silent"
Output : The strings are anagrams.


Input : s1 = "dad"
        s2 = "bad"
Output : The strings aren't anagrams.

'''

# The naive solution will be to sort he two strings and then check if they are equal. 
# The time complexity of the solution will be O(nlog(n))


# Let's look at a solutiuon with O(n), using array method


def anagrams(s1,s2):

    if len(s2) != len (s1):
        return False
    
    count_lst = [0]*255

    for i in range (len(s1)):
        count_lst[ord(s1[i])] = count_lst[ord(s1[i])] +1  # ek array ko 1 se badhao
        count_lst[ord(s2[i])] = count_lst[ord(s2[i])] -1 # doosre array ko 1 se ghatao
    
    for val in count_lst: # Final status of teh array will be alway 0 if it's an anagram
        if val!=0:
            return False
    return True
        

s1 = "listen"
s2 = "silen"
print(anagrams(s1,s2))
        


    









