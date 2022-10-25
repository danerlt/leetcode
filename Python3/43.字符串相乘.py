# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。 
# 
#  注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: num1 = "2", num2 = "3"
# 输出: "6" 
# 
#  示例 2: 
# 
#  
# 输入: num1 = "123", num2 = "456"
# 输出: "56088" 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= num1.length, num2.length <= 200 
#  num1 和 num2 只能由数字组成。 
#  num1 和 num2 都不包含任何前导零，除了数字0本身。 
#  
# 
#  Related Topics 数学 字符串 模拟 👍 1077 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        mult = self.str_to_num(num1) * self.str_to_num(num2)
        result = str(mult)
        return result

    def str_to_num(self, str_num: str) -> int:
        """将str转成int

        :param str_num: 数字字符串
        :return: 数字
        """
        if str_num.startswith("_"):
            raise Exception("参数为非负整数")
        str_map = {str(i): i for i in range(10)}
        if len(str_num) == 1:
            result = str_map[str_num]
        else:
            if str_num.startswith("0"):
                raise Exception("参数包含了前导0")
            num = 0
            for char in str_num:
                num = num * 10 + str_map[char]
            result = num
        return result


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    solution = Solution()
    solution.str_to_num("0")
    solution.str_to_num("1")
    solution.str_to_num("12")
    solution.str_to_num("123")
    solution.str_to_num("1235")
    solution.multiply("2", "3")
    solution.multiply("123", "456")
