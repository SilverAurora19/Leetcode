# LeetCode 141: 环形链表 (Linked List Cycle)
#
# 核心思路（快慢指针 / Floyd 判圈算法）：
# 慢指针每次走一步，快指针每次走两步。
#   - 如果没有环：快指针会先走到末尾（None），结束。
#   - 如果有环：快指针最终会追上慢指针（在环中相遇）。
#
# 直观理解：就像操场跑步，快的人最终会套圈追上慢的人。
#
# 时间复杂度：O(n)——有环时快指针最多比慢指针多跑一圈
# 空间复杂度：O(1)

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode | None
        :rtype: bool   # 链表是否有环
        """
        slow = head  # 慢指针，每次走 1 步
        fast = head  # 快指针，每次走 2 步

        # 只要快指针还没到末尾，就继续
        while fast is not None and fast.next is not None:
            slow = slow.next            # 慢指针走一步
            fast = fast.next.next       # 快指针走两步

            if slow is fast:            # 追上了 → 有环！
                return True

        # 快指针走到 None → 有尽头，无环
        return False
