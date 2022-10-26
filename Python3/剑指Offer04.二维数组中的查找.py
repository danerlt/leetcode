# 在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个
# 整数，判断数组中是否含有该整数。 
# 
#  
# 
#  示例: 
# 
#  现有矩阵 matrix 如下： 
# 
#  
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
#  
# 
#  给定 target = 5，返回 true。 
# 
#  给定 target = 20，返回 false。 
# 
#  
# 
#  限制： 
# 
#  0 <= n <= 1000 
# 
#  0 <= m <= 1000 
# 
#  
# 
#  注意：本题与主站 240 题相同：https://leetcode-cn.com/problems/search-a-2d-matrix-ii/ 
# 
#  Related Topics 数组 二分查找 分治 矩阵 👍 812 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        # 解题思路: 二分查找 中点在左下角的元组, 小于目标值在右面,大于目标值在上边
        if not matrix:
            return False
        rows = len(matrix)
        columns = len(matrix[0])
        row = rows - 1  # 行号
        column = 0  # 列号
        while 0 <= row < rows and 0 <= column < columns:
            temp = matrix[row][column]
            if temp == target:
                return True
            elif temp < target:
                # 右移
                column += 1
            else:
                # 上移
                row -= 1
        return False


# leetcode submit region end(Prohibit modification and deletion)

def t_solution(matrix, target):
    solution = Solution()
    res = solution.findNumberIn2DArray(matrix, target)
    print(res)


if __name__ == '__main__':
    m = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    t_solution(m, 5)
    t_solution(m, 20)
    t_solution([[]], 20)
    t_solution([[1, 2, 3]], 2)
    t_solution([[1, 2, 3]], 20)
