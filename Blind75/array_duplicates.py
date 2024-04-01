"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 
"""

def numa_array(nums):
    dict_num = {}
    dict_num [nums[0]] = 1
    for i in range(1,len(nums)):
        if nums[i] in dict_num:
            return True
        else:
            dict_num[nums[i]] = nums[i]

    if i ==len(nums)-1: # this is a redundant solution even a simple return False would do, since it woould mean that we have traversed all teh elements without exiting
        return False
    
# nums = [1,1,1,3,3,4,3,2,4,2]
# nums = [1,2,3,4]
nums = [1,2,3,1]
print(numa_array(nums))


