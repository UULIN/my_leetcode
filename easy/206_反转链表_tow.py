"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 申请两个节点，pre指向none，cur指向head
        pre = None
        cur = head
        while cur: # cur不为空
            # 记录当前节点的下一个节点为tmp
            tmp = cur.next
            # 将当前节点的下一个节点指向pre
            cur.next = pre
            # pre前进一位
            pre = cur
            # cur前进一位
            cur = tmp
        return pre

