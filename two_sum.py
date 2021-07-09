#!/usr/bin/python3

"""
Leetcode - 1. Two Sum (Easy)

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may
not use the same element twice.
You can return the answer in any order.
 
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    even_odd = None
    if not target % 2:
        even_odd = target // 2
    
    temp = {}
    for idx, num in enumerate(nums):
        diff = target - num
        if even_odd is not None and diff == num:
            try:
                return [temp[diff], idx]
            except KeyError:
                temp[num] = idx 
        else:
            temp[num] = idx
            if diff in temp:
                return [temp[diff], idx]


if __name__ == "__main__":
    int_array = input("Enter integers space separated: ")
    int_array = [int(i) for i in int_array.split()]
    target = int(input("Enter target number: "))
    print(twoSum(int_array, target))