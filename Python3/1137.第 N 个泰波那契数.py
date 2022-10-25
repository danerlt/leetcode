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
#  Related Topics 记忆化搜索 数学 动态规划 👍 223 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        cache = {0: 0, 1: 1, 2: 1}
        if n < 3:
            res = cache[n]
        else:
            for i in range(3, n+1):
                cache[i] = cache[i - 1] + cache[i - 2] + cache[i - 3]
            res = cache[n]
        return res


# leetcode submit region end(Prohibit modification and deletion)

def t_solution(n):
    solution = Solution()
    res = solution.tribonacci(n)
    print(f"n: {n}, res: {res}")


if __name__ == '__main__':
    t_solution(0)
    t_solution(1)
    t_solution(2)
    t_solution(3)
    t_solution(4)
    t_solution(25)
    t_solution(37)
