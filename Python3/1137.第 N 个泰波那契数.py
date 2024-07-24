# 泰波那契序列 Tn 定义如下： 
# 
#  T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2 
# 
#  给你整数 n，请返回第 n 个泰波那契数 Tn 的值。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 4
# 输出：4
# 解释：
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
#  
# 
#  示例 2： 
# 
#  输入：n = 25
# 输出：1389537
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= n <= 37 
#  答案保证是一个 32 位整数，即 answer <= 2^31 - 1。 
#  
# 
#  Related Topics 记忆化搜索 数学 动态规划 👍 307 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def tribonacci(self, n: int) -> int:
        # dp[i] 表示第i个泰波那契
        # dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        # 特殊值处理
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        # 初始化dp table
        dp = [0] * (n + 1)
        # 设置初始值
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        # 计算dp table
        for i in range(3, n + 1):
            dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

        res = dp[n]
        return res

# leetcode submit region end(Prohibit modification and deletion)

