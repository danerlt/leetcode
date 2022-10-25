# 实现 pow(x, n) ，即计算 x 的整数 n 次幂函数（即，xⁿ ）。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：x = 2.00000, n = 10
# 输出：1024.00000
#  
# 
#  示例 2： 
# 
#  
# 输入：x = 2.10000, n = 3
# 输出：9.26100
#  
# 
#  示例 3： 
# 
#  
# 输入：x = 2.00000, n = -2
# 输出：0.25000
# 解释：2-2 = 1/22 = 1/4 = 0.25
#  
# 
#  
# 
#  提示： 
# 
#  
#  -100.0 < x < 100.0 
#  -231 <= n <= 231-1 
#  -104 <= xⁿ <= 104 
#  
# 
#  Related Topics 递归 数学 👍 1060 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 如果n为偶数 x ^ n = x ^ (n /2 ) ^ 2 = (x ^ (n / 2)) * (x ^ (n / 2))
        # 如果n为奇数 将x ^ n = x ^ (n - 1) * x 然后装换成偶数计算

        if n == 0:
            return 1
        if n < 0:
            n = abs(n)
            flag = True  # 是否是负数幂
        else:
            flag = False

        ret = 1
        while n > 0:
            if n & 1 == 1:
                # 奇数
                ret *= x
            x *= x
            n = n >> 1
        if flag:
            ret = 1 / ret
        return ret


# leetcode submit region end(Prohibit modification and deletion)

def test_pow():
    solution = Solution()
    ret1 = solution.myPow(2.00000, 10)
    print(ret1)
    ret2 = solution.myPow(2.10000, 3)
    print(ret2)
    ret3 = solution.myPow(2.00000, -2)
    print(ret3)
    ret4 = solution.myPow(0.00001, 2 ** 31)
    print(ret4)


if __name__ == '__main__':
    test_pow()
