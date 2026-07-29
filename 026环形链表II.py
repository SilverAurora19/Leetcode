# LeetCode 142: 环形链表 II (Linked List Cycle II)
#
# 核心思路（快慢指针，两阶段）：
#
# 阶段1 —— 判断是否有环（同 141）：
#   慢指针每次走 1 步，快指针每次走 2 步。
#   如果两指针相遇，说明有环（记相遇点为 meet）。
#
# 阶段2 —— 找到环的入口：
#   相遇后，把一个指针放回头节点 head，另一个留在相遇点。
#   两个指针都改为每次走 1 步，它们再次相遇的位置就是环的入口。
#
# 数学原理：
#   设 头→环入口 距离为 a，环入口→相遇点 距离为 b，相遇点→环入口（绕一圈回）距离为 c。
#   快指针路程 = a + b + n(b + c)  （走了 n 圈环）
#   慢指针路程 = a + b
#   快指针速度是慢指针 2 倍，所以：a + b + n(b + c) = 2(a + b)
#   → a + b = n(b + c)
#   → a = (n-1)(b + c) + c
#   意味着：从头到环入口的距离 a，等于从相遇点绕若干圈后再走 c 的距离。
#   所以从 head 和 meet 同时出发，每次各走 1 步，必在环入口相遇。
#
# 时间复杂度：O(n)
# 空间复杂度：O(1)

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode | None
        :rtype: ListNode | None   # 返回环的入口节点，无环则返回 None
        """
        slow = head
        fast = head

        # 阶段1：快慢指针找环，找到相遇点
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:                          # 相遇 → 有环
                # 阶段2：一个指针回头，另一个留在相遇点，同步走
                entry_pointer = head                  # 从链表头出发

                while slow is not entry_pointer:      # 两指针都走1步，直到相遇
                    entry_pointer = entry_pointer.next
                    slow = slow.next

                return entry_pointer                  # 相遇点即环入口

        # 快指针走到 None，无环
        return None
