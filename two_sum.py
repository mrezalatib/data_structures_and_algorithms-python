"""
Problem: Two Sum

Description:
Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to the target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
Example:
Input:

nums = [2, 7, 11, 15], target = 9
Output:

[0, 1]

Explanation: Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].
Input:

nums = [3, 2, 4], target = 6
Output:

[1, 2]
Input:

nums = [3, 3], target = 6
Output:

[0, 1]
"""

def two_sum(nums, target):

    # my_num_dictioanry = {}
    # index = 0

    # for number in nums:
    #     my_num_dictioanry[index] = number
    #     index += 1

    # return my_num_dictioanry

    for number in nums:
        if target - number in nums:
            return number
            
        
print(two_sum([3, 2, 4], 6))