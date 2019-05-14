#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
        
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        queue = [root]
        while queue:
            temp =[]
            row = []
            for node in queue:
                row.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:    
                    temp.append(node.right)
            queue = temp        
            res.insert(0, row)      
        return res

