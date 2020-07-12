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
    # 双指针迭代法实现
    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # 申请两个指针 cur 和pre ，pre指向None
        pre = None
        cur = head
        # 进行指针反转
        while cur:  # 当cur一直有值时
            # 设置一个tmp存储cur的临时值,记录当前节点的下一个节点
            tmp = cur.next
            # 将当前节点指向pre
            cur.next = pre
            # 将pre前移一位
            pre = cur
            # 将cur前移一位
            cur = tmp
        return pre
    # 递归法实现
    def reverseList2(self, head):
        """

        :param head:头指针
        :return:
        """
        # 退出条件，当前节点或下一个节点为空
        if head is None or head.next is None:
            return head
        # cur代表当前链表最后一个值
        cur = self.reverseList2(head.next)
        # 如果链表是 1->2->3->4->5，那么此时的cur就是5
        # 而head是4，head的下一个是5，下下一个是空
        head.next.next = head
        # 防止链表循环，需要将head.next设置为空
        head.next = None
        # 每层递归函数都返回cur，也就是最后一个节点
        return cur
