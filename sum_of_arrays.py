"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order """


# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

# Step 1 via brute force

nums = [2,7,11,15]
target = 9

def funct():
    for val1 in nums:
        for val2 in nums:
            if (val1 + val2) == target:
                print([val1,val2])
            break

# Step 2 using has map in python

def func1():        
    dictnum = {}

    for i,num in enumerate (nums):
        complement = target - num
 
        if complement in dictnum:  # ye dict ka keys check krta hai in O(1)
            return  ([dictnum[complement],i])
        
        dictnum[num] =i
    
print(func1())


    
