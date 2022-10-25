# 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 13
# 输出：6
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 0
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= n <= 10⁹ 
#  
# 
#  Related Topics 递归 数学 动态规划 👍 472 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    cache = {0: 0}

    def countOne(self, n: int) -> int:
        str_n = str(n)
        from collections import Counter
        c = Counter(str_n)
        count = c.get("1", 0)
        return count

    def countDigitOne(self, n: int) -> int:
        for num in range(1, n + 1):
            self.cache[num] = self.countOne(num) + self.cache[num - 1]

        return self.cache[n]


# leetcode submit region end(Prohibit modification and deletion)
def t_solution(num):
    solution = Solution()
    ret = solution.countDigitOne(num)
    print(ret)


if __name__ == '__main__':
    t_solution(0)
    t_solution(1)
    t_solution(2)
    t_solution(3)
    t_solution(10)
    t_solution(11)
    t_solution(100)
    t_solution(10000000)
