# 给你一个字符串 columnTitle ，表示 Excel 表格中的列名称。返回 该列名称对应的列序号 。 
# 
#  例如： 
# 
#  
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ... 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: columnTitle = "A"
# 输出: 1
#  
# 
#  示例 2: 
# 
#  
# 输入: columnTitle = "AB"
# 输出: 28
#  
# 
#  示例 3: 
# 
#  
# 输入: columnTitle = "ZY"
# 输出: 701 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= columnTitle.length <= 7 
#  columnTitle 仅由大写英文组成 
#  columnTitle 在范围 ["A", "FXSHRXW"] 内 
#  
# 
#  Related Topics 数学 字符串 👍 356 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        char_dict = {chr(ord("A") + i): i + 1 for i in range(26)}

        res = 0
        length = len(columnTitle)
        if length == 1:
            res = char_dict[columnTitle]
        else:
            mi = 0
            for index in range(length - 1, -1, -1):
                char = columnTitle[index]
                num = char_dict[char]
                num = (26 ** mi) * num
                mi += 1
                res += num
        return res


# leetcode submit region end(Prohibit modification and deletion)

def t_solution(column_title):
    solution = Solution()
    res = solution.titleToNumber(column_title)
    print(res)


if __name__ == '__main__':
    t_solution("A")
    t_solution("Z")
    t_solution("AA")
    t_solution("AB")
    t_solution("ZY")
    t_solution("FXSHRXW")
