#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # dp[i][j] 表示起点到坐标i,j的路径数
        # dp[0][0] = 1
        # 如果上面为障碍物则等于左边的，如果左边为障碍物，则等于上面的，如果左边和上面都为障碍物则路径为0
        # dp[i][j] = dp[i-1][j] + dp[i][j-1] 
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * (n+1) for i in range(m+1)]
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] += dp[i][j-1] + dp[i-1][j] 
                else:
                    dp[i][j] = 0    
        return dp[m-1][n-1]

