# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。 
# 
#  
# 
#  示例 1： 
# 
#  输入：head = [1,3,2]
# 输出：[2,3,1] 
# 
#  
# 
#  限制： 
# 
#  0 <= 链表长度 <= 10000 
# 
#  Related Topics 栈 递归 链表 双指针 👍 347 👎 0
from collections import deque
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        # 利用栈实现 Python中使用deque
        stack = deque()
        while head:
            stack.append(head.val)
            head = head.next
        res = []
        while len(stack) > 0:
            res.append(stack.pop())
        return res


# leetcode submit region end(Prohibit modification and deletion)

def t_solution(head):
    so = Solution()
    res = so.reversePrint(head)
    print(res)


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(3)
    head.next = ListNode(2)
    t_solution(head)
    t_solution(None)
