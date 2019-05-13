#
# @lc app=leetcode.cn id=908 lang=python3
#
# [908] 最小差值 I
#
class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        # 思路，先排序，找到最小值和最大值，用a=最小值+K和b=最大值-K，
        # 如果a < b，结果就是b - a，否则就是0
        A.sort() # 先排序
        min, max = A[0], A[-1]
        min_temp, max_temp = min + K, max - K
        if min_temp < max_temp:
            return max_temp - min_temp
        else:
            return 0

