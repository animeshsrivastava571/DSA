'''
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
Vowel letters in English are 'a','e','i','o', and 'u'.
Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

'''


def max_vowels(str1, k):

    lst_vowel = ['a','e','i','o','u']  # this is the brute force way of solving this
    cnt_max =0
    for i in range(len(str1)-k+1):
        substr = str1[i:i+k]
        cnt = 0
        
        for elem in substr:
            if elem in lst_vowel:
                cnt = cnt+1
        if cnt>cnt_max:
            cnt_max = cnt
    return cnt_max

s = "abciiidef"
k = 3

s = "leetcode"
k = 2
#print(max_vowels(s, k))


#Optimised way of solving using sliding window method
'''
Here are the steps to implement this approach:

Initialize a set of vowels for quick look-up.
Start by counting the number of vowels in the first substring of length k.
As you slide the window by one position to the right, add one to the count if the incoming character is a vowel and subtract one if the outgoing character is a vowel.
Update the maximum number of vowels found so far.
This way, you don't have to check each substring from scratch; you just update the count based on the characters that are entering and exiting the window as it slides. This makes the solution very efficient because each character in s is processed exactly once.

'''

s = "abciiidef"
k = 3

def max_vowels_optimised(str1, k):

    set_vowel = set('aeiou')  # optimised way using sliding window approach
    cnt_max =0
    t = 0
    for elem in s[:k]:
        if elem in set_vowel:
            t = t+1
    
    cnt_max = t
    for i in range (k,len(s)):
        if s[i] in set_vowel:
            t = t+1
        if s[i-k] in set_vowel:
            t = t-1

        if t>cnt_max:
            cnt_max=t
    return cnt_max

s = "ibpbhixfiouhdljnjfflpapptrxgcomvnb"
k = 33
print(max_vowels_optimised(s, k))