#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 解题思路
        # 利用滑动窗口，[i,j)表示子串，如果s[j]没在里面，j++，将s[j]加入到set中
        # 如果s[j]在里面，set中移除s[i],i++,
        
        
        sub = set()
        i = j = 0
        n = len(s)
        res = 0
        while i < n and j < n:
            if s[j] not in sub:
                sub.add(s[j])
                j += 1
                res = max(res, j-i)
            else:
                sub.remove(s[i])
                i += 1
        return res
        

