#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
class Solution:
    def maxArea(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1 # 左右两条线的下标
        res = 0
        width = len(height) - 1
        for w in range(width, 0, -1):
            if height[L] < height[R]:
                # 左边的高度小，面积为左边的高度乘以宽度
                res = max(res, height[L] * w)
                L += 1
            else:
                # 右边的高度小，面积等于右面的高度乘以宽度
                res = max(res, height[R] * w)    
                R -= 1
        return res    
