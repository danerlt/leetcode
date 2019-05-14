#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        nodes = [root]
        for node in nodes:
            if node:
                nodes.extend([node.left, node.right])
        
        nodes.reverse()
        depths = {None:0}
        for node in nodes:
            if node:
                depths[node] = max(depths.get(node.left, 0), depths.get(node.right, 0)) + 1                
                if abs(depths.get(node.left, 0) - depths.get(node.right, 0)) > 1:
                    return False
        return True        
                  

