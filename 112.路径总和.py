#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        t = sum - root.val
        if not root.left and not root.right:
            return t == 0
        return self.hasPathSum(root.left, t) or self.hasPathSum(root.right, t)

