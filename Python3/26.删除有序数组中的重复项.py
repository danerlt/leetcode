# 给你一个 升序排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 
# 。 
# 
#  由于在某些语言中不能改变数组的长度，所以必须将结果放在数组nums的第一部分。更规范地说，如果在删除重复项之后有 k 个元素，那么 nums 的前 k 个
# 元素应该保存最终结果。 
# 
#  将最终结果插入 nums 的前 k 个位置后返回 k 。 
# 
#  不要使用额外的空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。 
# 
#  判题标准: 
# 
#  系统会用下面的代码来测试你的题解: 
# 
#  
# int[] nums = [...]; // 输入数组
# int[] expectedNums = [...]; // 长度正确的期望答案
# 
# int k = removeDuplicates(nums); // 调用
# 
# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# } 
# 
#  如果所有断言都通过，那么您的题解将被 通过。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,2]
# 输出：2, nums = [1,2,_]
# 解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,0,1,1,1,2,2,3,3,4]
# 输出：5, nums = [0,1,2,3,4]
# 解释：函数应该de返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 3 * 10⁴ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  nums 已按 升序 排列 
#  
# 
#  Related Topics 数组 双指针 👍 2913 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 解题思路 双指针
        # 开始的时候faster和lower都从0开始
        # 如果faster和lower对应的值相同那么，faster++
        # 如果faster对应的值大于lower，先lower++ 然后交换lower和faster的对应值 然后,faster++
        if not nums: return 0
        lower, faster = 0, 0

        while faster < len(nums):
            if nums[faster] > nums[lower]:
                lower += 1
                nums[lower], nums[faster] = nums[faster], nums[lower]
                faster += 1
            else:
                faster += 1

        return lower+1


# leetcode submit region end(Prohibit modification and deletion)

def t_solution(nums):
    so = Solution()
    res = so.removeDuplicates(nums)
    print(res, nums)


if __name__ == '__main__':
    t_solution([])
    t_solution([1, 1, 2])
    t_solution([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    t_solution([0, 0, 1, 1, 1, 2, 2, 3, 4, 5, 5, 6])
