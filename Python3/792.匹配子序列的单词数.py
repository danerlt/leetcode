# 给定字符串 s 和字符串数组 words, 返回 words[i] 中是s的子序列的单词个数 。 
# 
#  字符串的 子序列 是从原始字符串中生成的新字符串，可以从中删去一些字符(可以是none)，而不改变其余字符的相对顺序。 
# 
#  
#  例如， “ace” 是 “abcde” 的子序列。 
#  
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "abcde", words = ["a","bb","acd","ace"]
# 输出: 3
# 解释: 有三个是 s 的子序列的单词: "a", "acd", "ace"。
#  
# 
#  Example 2: 
# 
#  
# 输入: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
# 输出: 2
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= s.length <= 5 * 10⁴ 
#  1 <= words.length <= 5000 
#  1 <= words[i].length <= 50 
#  words[i]和 s 都只由小写字母组成。 
#  
# 
# 
#  Related Topics 字典树 哈希表 字符串 排序 👍 274 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        res = 0
        cache = {}
        for word in words:
            if word not in cache:
                cache[word] = 1
            else:
                cache[word] += 1
        for word, num in cache.items():
            if self.is_sub_string(s, word):
                res += num
        return res

    def is_sub_string(self, origin: str, sub: str) -> bool:
        sub_length = len(sub)
        origin_length = len(origin)
        # 如果子串长度大于原来的字符串 直接返回False
        if sub_length > origin_length:
            return False
        # 如果子串和原来的字符串相等 直接返回True
        if origin == sub:
            return True
        # 用两个指针分别扫描字符串
        origin_index = 0
        sub_index = 0
        while sub_index < sub_length and origin_index < origin_length:
            # 如果指针对应位置的字符串相等,则两个指针都后移一般,否则只有原来的字符串后移
            if sub[sub_index] == origin[origin_index]:
                sub_index += 1
                origin_index += 1
            else:
                origin_index += 1
        # 循环结束 如果是子串扫描完了,那么说明是子序列,否则就不是子序列
        if sub_index == sub_length:
            return True
        else:
            return False
# leetcode submit region end(Prohibit modification and deletion)
