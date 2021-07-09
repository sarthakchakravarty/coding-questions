#!/usr/bin/python3

"""
Leetcode - 2. Add Two Numbers (Medium)

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a
single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except 
the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    a = l1.val if l1 else 0
    b = l2.val if l2 else 0
    sum_ab = a + b
    if sum_ab == 10:
        sum_ab = 0
        carry = 1
    elif sum_ab // 10:
        sum_ab %= 10
        carry = 1
    else:
        carry = 0
    res = ListNode(sum_ab)
    l1 = l1.next
    l2 = l2.next
    current = res
    while(l1 and l2):
        a = l1.val
        b = l2.val
        sum_ab = a + b + carry
        if sum_ab == 10:
            sum_ab = 0
            carry = 1
        elif sum_ab // 10:
            sum_ab %= 10
            carry = 1
        else:
            carry = 0
        temp = ListNode(sum_ab)
        current.next = temp
        current = temp
        l1 = l1.next
        l2 = l2.next
    
    if l1 or l2:
        remain = l1 if l1 else l2
        while(remain):
            a = remain.val
            if carry:
                a += carry
                if a == 10:
                    a = 0
                    carry = 1
                else:
                    carry = 0
            temp = ListNode(a)
            current.next = temp
            current = temp
            remain = remain.next

    if carry:
        temp = ListNode(1)
        current.next = temp
        current = temp
    return res
