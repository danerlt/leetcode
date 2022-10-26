# 输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。 
# 
#  假设输入的前序遍历和中序遍历的结果中都不含重复的数字。 
# 
#  
# 
#  示例 1: 
#  
#  
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
#  
# 
#  示例 2: 
# 
#  
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
#  
# 
#  
# 
#  限制： 
# 
#  0 <= 节点个数 <= 5000 
# 
#  
# 
#  注意：本题与主站 105 题重复：https://leetcode-cn.com/problems/construct-binary-tree-from-
# preorder-and-inorder-traversal/ 
# 
#  Related Topics 树 数组 哈希表 分治 二叉树 👍 930 👎 0
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 解题思路:
        # preorder的第一个元素是根节点
        # 然后在inorder中找到根节点的,在根节点左边就是左子树,根节点的右边就是右子数
        # 然后递归处理
        # 在inorder找根节点下标可以用dict,比用list性能更好
        def helper(pre_left: int, pre_right: int, in_left, in_right):
            """内部函数

            :param pre_left: 先序遍历起始下标
            :param pre_right: 先序遍历结束下标
            :param in_left: 中序遍历起始下标
            :param in_right: 中序遍历结束下标
            :return: 根节点
            """
            if pre_left > pre_right:
                return None
            # 前序遍历中的第一个节点就是根节点 preorder_root = preorder_left
            pre_root_index = pre_left
            root_val = preorder[pre_root_index]
            in_root_index = cache[root_val]  # 根节点在中序遍历的下标

            # 先构造根节点
            root = TreeNode(root_val)
            sub_left_cout = in_root_index - in_left  # 左子树的数量

            root.left = helper(pre_left + 1, pre_root_index + sub_left_cout, in_left, in_root_index - 1)
            root.right = helper(pre_root_index + sub_left_cout + 1, pre_right, in_root_index + 1, in_right)
            return root

        # 构造中序遍历字典 key是数字, value是下标
        cache = {ele: index for index, ele in enumerate(inorder)}
        n = len(preorder)
        res = helper(0, n - 1, 0, n - 1)
        return res


# leetcode submit region end(Prohibit modification and deletion)


def get_preorder_list(root):
    res = []
    if not root:
        return []
    else:
        res.append(root.val)
        res.extend(get_preorder_list(root.left))
        res.extend(get_preorder_list(root.right))
        return res


def t_solutin(preorder, inorder):
    so = Solution()
    res = so.buildTree(preorder, inorder)
    pre_list = get_preorder_list(res)
    print(pre_list)


if __name__ == '__main__':
    t_solutin([], [])
    t_solutin([-1], [-1])
    t_solutin([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
