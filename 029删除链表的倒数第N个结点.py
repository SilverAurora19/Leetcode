# LeetCode 19: 删除链表的倒数第 N 个结点 (Remove Nth Node From End of List)
#
# 核心思路（快慢指针，间隔 N+1）：
# 让 fast 先走 n+1 步，然后 slow 和 fast 同步走。
# 当 fast 走到尾（None）时，slow 正好在"待删节点的前一个节点"，
# 这样就可以直接跳过待删节点：slow.next = slow.next.next
#
# 为什么是 n+1 而不是 n？
#   因为要删的节点是倒数第 N 个，我们需要停在它的前驱节点。
#   多走一步，slow 就能刚好落在倒数第 N+1 个。
#
# dummy 的作用：
#   当要删的恰好是头节点时（如链表长度 = n），需要 dummy 来充当"头的前驱"。
#
# 例如：head = 1→2→3→4→5, n = 2（删倒数第 2 个即 4）
#   初始：dummy → 1 → 2 → 3 → 4 → 5
#   fast 先走 3 步：fast 指向 3
#   slow/fast 同步走：fast 到 None 时 slow 停在 3
#   slow.next = slow.next.next  → 跳过 4
#   结果：1 → 2 → 3 → 5
#
# 时间复杂度：O(n)，一趟遍历
# 空间复杂度：O(1)

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode | None   # 删除后的链表头
        """
        # dummy 指向 head，处理"删头节点"的边界情况
        dummy = ListNode(0, head)

        fast = dummy
        slow = dummy

        # 第1步：fast 先走 n+1 步，制造 n+1 的间隔
        #        这样 slow 最终停在待删节点的前驱
        for _ in range(n + 1):
            fast = fast.next

        # 第2步：fast 和 slow 同步走，直到 fast 走到末尾
        while fast is not None:
            fast = fast.next
            slow = slow.next

        # 第3步：此时 slow 指向待删节点的前驱，跳过目标节点
        slow.next = slow.next.next

        return dummy.next  # 返回真正的头（可能还是 head，也可能被删了）
