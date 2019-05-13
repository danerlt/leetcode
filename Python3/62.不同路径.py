#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j] 表示左上角到点i,j的路径数
        # dp[i][j] = dp[i-1][j] + dp[i][j-1] 
        # dp[i][0] = 1
        # dp[0][j] = 1
        dp = [[1]*n for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] 
                    
        return dp[m-1][n-1]        

