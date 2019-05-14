#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        curr = res
        ops = 0 # 进位\
        while True:
            temp = ops
            if not l1 and not l2: break
            if l1:
                temp += l1.val 
                l1 = l1.next
            if l2:
                temp += l2.val
                l2 = l2.next  
            ops = temp // 10 # 进位
            temp = temp % 10 # 个位
            curr.next = ListNode(temp)
            curr = curr.next
        if ops != 0:
            curr.next = ListNode(ops)
        return res.next

