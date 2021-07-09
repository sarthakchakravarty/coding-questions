#!/usr/bin/python3

"""
Leetcode - 3. Longest Substring Without Repeating Characters (Medium)

Given a string s, find the length of the longest substring without 
repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and 
not a substring.

Example 4:
Input: s = ""
Output: 0

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0
    elif not s[1:2]:
        return 1
    else:
        start = 0
        max_len = 0
        s_len = len(s)
        while(start < s_len):
            unique = set()
            counter = 0
            for i in s[start:]:
                if i not in unique:
                    unique.add(i)
                    counter += 1
                else:
                    max_len = counter if counter >= max_len else max_len
                    start += 1
                    break
            else:
                max_len = counter if counter >= max_len else max_len
                break
        return max_len


if __name__ == '__main__':
    s = input("Enter string: ")
    print(lengthOfLongestSubstring(s))