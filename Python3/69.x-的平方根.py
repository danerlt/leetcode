#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        # j = x / 2 + 1 的原因： 因为(x/2+1)^2 = x^2/4 + x + 1 > x,所以只需要从x/2+1为结束值
        i = 1; j = x // 2 + 1
        while( i <= j ):
            center = ( i + j ) // 2
            if center ** 2 == x:
                return center
            elif center ** 2 > x:
                j = center - 1
            else:
                i = center + 1
        return j

