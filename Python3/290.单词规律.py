# 给定一种规律 pattern 和一个字符串 s ，判断 s 是否遵循相同的规律。 
# 
#  这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 s 中的每个非空单词之间存在着双向连接的对应规律。 
# 
#  
# 
#  示例1: 
# 
#  
# 输入: pattern = "abba", s = "dog cat cat dog"
# 输出: true 
# 
#  示例 2: 
# 
#  
# 输入:pattern = "abba", s = "dog cat cat fish"
# 输出: false 
# 
#  示例 3: 
# 
#  
# 输入: pattern = "aaaa", s = "dog cat cat dog"
# 输出: false 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= pattern.length <= 300 
#  pattern 只包含小写英文字母 
#  1 <= s.length <= 3000 
#  s 只包含小写英文字母和 ' ' 
#  s 不包含 任何前导或尾随对空格 
#  s 中每个单词都被 单个空格 分隔 
#  
# 
#  Related Topics 哈希表 字符串 👍 512 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        # 需要注意 pattern中的字母和s中的单字是双向连接, 所以要用两个dict
        arr = s.split(" ")
        if len(arr) != len(pattern):
            return False
        word_dict = {}
        char_dict = {}
        for index, char in enumerate(pattern):
            word = arr[index]
            if char not in char_dict and word not in word_dict:
                char_dict[char] = word
                word_dict[word] = char
            else:
                if char in char_dict and word != char_dict[char]:
                    return False
                if word in word_dict and char != word_dict[word]:
                    return False
        return True


# leetcode submit region end(Prohibit modification and deletion)


def t_solution(pattern, s):
    solution = Solution()
    res = solution.wordPattern(pattern, s)
    print(res)


if __name__ == '__main__':
    t_solution("aabb", "dog dog cat cat")
    t_solution("abba", "dog cat cat dog dog")
    t_solution("aaaa", "dog cat cat dog")
    t_solution("abba", "dog dog dog dog")
