# LeetCode 160: 相交链表 (Intersection of Two Linked Lists)
#
# 核心思路（双指针交替遍历）：
# 两个指针 pA 和 pB 分别从 headA 和 headB 出发：
#   - pA 走完 A 链后，跳到 B 链的头继续走
#   - pB 走完 B 链后，跳到 A 链的头继续走
#
# 这样两指针走过的总路程相等（都是 len(A) + len(B)），因此：
#   - 如果有交点：它们一定会在交点处同时相遇
#   - 如果无交点：它们会同时走到 None，退出循环
#
# 直观理解：
#   自己跑完了换别人的头跑，两边步长一致，必在交叉处碰头。
#
# 时间复杂度：O(m + n)
# 空间复杂度：O(1)

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode | None   # 相交节点，无交点则返回 None
        """
        pointer_a = headA
        pointer_b = headB

        # 当两指针指向相同节点（或同时为 None）时退出
        while pointer_a is not pointer_b:
            # pA：走到尾了就跳到 B 链的头，否则继续往前走
            if pointer_a is None:
                pointer_a = headB
            else:
                pointer_a = pointer_a.next

            # pB：走到尾了就跳到 A 链的头，否则继续往前走
            if pointer_b is None:
                pointer_b = headA
            else:
                pointer_b = pointer_b.next

        # 要么是交点，要么是 None（无交点）
        return pointer_a
