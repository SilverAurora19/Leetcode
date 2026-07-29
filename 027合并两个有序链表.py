# LeetCode 21: 合并两个有序链表 (Merge Two Sorted Lists)
#
# 核心思路（双指针 + 虚拟头节点）：
# 同时遍历两个有序链表，每次比较当前节点值，把较小的接到结果链上。
# 其中一个链表走完后，把另一个没走完的直接挂在末尾（因为它本身已经有序）。
#
# dummy 节点的作用：避免处理"头节点为空"的特殊情况，简化代码。
#
# 时间复杂度：O(m + n)
# 空间复杂度：O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: ListNode | None
        :type list2: ListNode | None
        :rtype: ListNode | None   # 合并后的有序链表头
        """
        dummy = ListNode()         # 虚拟头节点，避免处理空链表特殊情况
        tail = dummy               # tail 始终指向结果链的最后一个节点

        # 两链表都还有节点时，比较并取较小者接入
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:    # list1 的值更小
                tail.next = list1         # 把 list1 当前节点接入
                list1 = list1.next        # list1 指针前进
            else:                         # list2 的值更小
                tail.next = list2         # 把 list2 当前节点接入
                list2 = list2.next        # list2 指针前进

            tail = tail.next              # tail 指针前进

        # 其中一条链已空，把剩余链直接接上（无需逐节点处理）
        if list1 is not None:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next  # 真实头节点是 dummy 的下一个
