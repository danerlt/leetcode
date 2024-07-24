# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。 
# 
#  每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？ 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 2
# 输出：2
# 解释：有两种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶
# 2. 2 阶 
# 
#  示例 2： 
# 
#  
# 输入：n = 3
# 输出：3
# 解释：有三种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶 + 1 阶
# 2. 1 阶 + 2 阶
# 3. 2 阶 + 1 阶
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 45 
#  
# 
#  Related Topics 记忆化搜索 数学 动态规划 👍 3558 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i] 表示爬上第i阶楼梯的方法
        # 对于第i阶来说，有2种情况，将每种情况的方法加起来就是最终结果
        # 从第i-1阶爬，然后爬1个台阶，这是一种方法
        # 从第i-2阶爬，然后爬2个台阶，这是一种方法
        # 所以dp[i] = dp[i-1] + dp[i-2]


        # 初始值特殊处理
        if n == 1:
            return 1
        elif n == 2:
            return 2

        # 初始化dp table
        dp = [0] * (n + 1)
        # 设置初始值
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        result = dp[n]
        return result
# leetcode submit region end(Prohibit modification and deletion)

