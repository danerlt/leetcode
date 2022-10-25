# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。 
# 
#  字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而
# "aec"不是）。 
# 
#  进阶： 
# 
#  如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代
# 码？ 
# 
#  致谢： 
# 
#  特别感谢 @pbrother 添加此问题并且创建所有测试用例。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "abc", t = "ahbgdc"
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "axc", t = "ahbgdc"
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 100 
#  0 <= t.length <= 10^4 
#  两个字符串都只由小写字符组成。 
#  
# 
#  Related Topics 双指针 字符串 动态规划 👍 745 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isSubsequence(self, s, t):
        """

        慢指针循环子串s,快指针循环主串
        如果在主串t找到s的字符,则慢指针+1,快指针等于t的下标加1
        如果主串扫描完没找到相等的字符说明不匹配,直接返回False
        如果慢指针扫描完没返回False就说明匹配成功,返回True
        :type s: str
        :type t: str
        :rtype: bool
        """

        low = 0  # 慢指针
        fast = 0  # 快指针
        length_s = len(s)
        length_t = len(t)
        while low < length_s:
            sub_char = s[low]
            is_find = False
            for index in range(fast, length_t):
                main_char = t[index]
                if sub_char == main_char:
                    low += 1
                    fast = index + 1
                    is_find = True
                    break
            if not is_find:
                return False
        return True


# leetcode submit region end(Prohibit modification and deletion)

def t_solution(s, t):
    solution = Solution()
    res = solution.isSubsequence(s, t)
    print(res)


if __name__ == '__main__':
    t_solution("", "")
    t_solution("aaa", "")
    t_solution("", "bbb")
    t_solution("abc", "ahbgdc")
    t_solution("axc", "ahbgdc")
