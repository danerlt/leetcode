#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:return head
        pre, post = head, head.next
        while post is not None:
            if pre.val == post.val:
                pre.next = post.next
                post = pre.next
            else:
                post = post.next
                pre = pre.next
        return head

