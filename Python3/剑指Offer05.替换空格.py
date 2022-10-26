# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "We are happy."
# 输出："We.are%20happy."
# 
#  
# 
#  限制： 
# 
#  0 <= s 的长度 <= 10000 
# 
#  Related Topics 字符串 👍 360 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def replaceSpace(self, s: str) -> str:
        # 解题思路
        # 创建一个list,循环字符串,如果为空格就append%20,否则就append字符
        res = []
        for char in s:
            if char == " ":
                res.append("%20")
            else:
                res.append(char)
        res = "".join(res)
        return res
# leetcode submit region end(Prohibit modification and deletion)
