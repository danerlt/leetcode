# 给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。 
# 
#  你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。 
# 
#  请你计算并返回达到楼梯顶部的最低花费。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：cost = [10,15,20]
# 输出：15
# 解释：你将从下标为 1 的台阶开始。
# - 支付 15 ，向上爬两个台阶，到达楼梯顶部。
# 总花费为 15 。
#  
# 
#  示例 2： 
# 
#  
# 输入：cost = [1,100,1,1,1,100,1,1,100,1]
# 输出：6
# 解释：你将从下标为 0 的台阶开始。
# - 支付 1 ，向上爬两个台阶，到达下标为 2 的台阶。
# - 支付 1 ，向上爬两个台阶，到达下标为 4 的台阶。
# - 支付 1 ，向上爬两个台阶，到达下标为 6 的台阶。
# - 支付 1 ，向上爬一个台阶，到达下标为 7 的台阶。
# - 支付 1 ，向上爬两个台阶，到达下标为 9 的台阶。
# - 支付 1 ，向上爬一个台阶，到达楼梯顶部。
# 总花费为 6 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= cost.length <= 1000 
#  0 <= cost[i] <= 999 
#  
# 
#  Related Topics 数组 动态规划 👍 1031 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        对于第n阶台阶来说 最低花费为 当前台阶花费 + min(n-1阶台阶花费, n-2阶台阶花费)
        :type cost: List[int]
        :rtype: int
        """
        # 当没有台阶时花费为0
        # 当只有一个台阶时,直接到台阶顶,花费也为0
        if len(cost) <= 1:
            return 0
        cache = [0] * len(cost)

        for index, current_cost in enumerate(cost):
            if index == 0:
                cache[0] = cost[0]
            elif index == 1:
                cache[1] = min(current_cost, current_cost + cache[0])
            else:
                cache[index] = current_cost + min(cache[index - 1], cache[index - 2])

        res = min(cache[-1], cache[-2])
        return res


# leetcode submit region end(Prohibit modification and deletion)

def t_solution(cost):
    solution = Solution()
    res = solution.minCostClimbingStairs(cost)
    print(res)


if __name__ == '__main__':
    t_solution([])
    t_solution([1])
    t_solution([1, 2])
    t_solution([10, 15, 20])
    t_solution([10, 15, 20, 1])
    t_solution([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
