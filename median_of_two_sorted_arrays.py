#!/usr/bin/python3

"""
Leetcode - 4. Median of Two Sorted Arrays (Hard)

Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:
Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000

Example 4:
Input: nums1 = [], nums2 = [1]
Output: 1.00000

Example 5:
Input: nums1 = [2], nums2 = []
Output: 2.00000

Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""


def mergeSortedArray(nums1, nums2):
    if not nums1:
        return nums2
    elif not nums2:
        return nums1
    else:
        nums1_ptr, nums2_ptr = 0, 0
        merge_arr = []
        nums1_len, nums2_len = len(nums1), len(nums2)
        while (nums1_ptr < nums1_len) and (nums2_ptr < nums2_len):
            if nums1[nums1_ptr] <= nums2[nums2_ptr]:
                merge_arr.append(nums1[nums1_ptr])
                nums1_ptr += 1
            else:
                merge_arr.append(nums2[nums2_ptr])
                nums2_ptr += 1
        if nums1_ptr != nums1_len:
            merge_arr.extend(nums1[nums1_ptr: ])
        else:
            merge_arr.extend(nums2[nums2_ptr: ])
        return merge_arr


def findMedianSortedArrays(nums1, nums2):
    if not nums1 and not nums2:
        return 0.0
    merged_arr = mergeSortedArray(nums1, nums2)
    merged_arr_len = len(merged_arr)
    if not merged_arr_len % 2:
        mid_elm = merged_arr_len // 2
        return (merged_arr[mid_elm] + merged_arr[mid_elm - 1]) / 2
    else:
        return float(merged_arr[merged_arr_len // 2])


if __name__ == '__main__':
    nums1 = [int(i) for i in input("Enter numbers space separated: ").split()]
    nums2 = [int(i) for i in input("Enter numbers space separated: ").split()]

    print(findMedianSortedArrays(nums1, nums2))