# LeetCode 24: 两两交换链表中的节点 (Swap Nodes in Pairs)
#
# 核心思路（三指针 + dummy）：
# 用 previous 指向每对节点的前驱，然后重新编排两个节点的 next 指向。
#
# 例如：head = 1→2→3→4
#              pre  first  second
#   初始：dummy → 1 → 2 → 3 → 4
#
#   交换步骤：
#     first.next = second.next   // 1 指向 3
#     second.next = first        // 2 指向 1
#     pre.next = second          // dummy 指向 2
#     结果：dummy → 2 → 1 → 3 → 4
#
#   然后 pre 移到 1（即 first，交换后是当前对的第二个节点），继续下一轮。
#
# 时间复杂度：O(n)
# 空间复杂度：O(1)

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode | None
        :rtype: ListNode | None   # 交换后的链表头
        """
        dummy = ListNode(0, head)   # 虚拟头，简化头节点交换
        previous = dummy            # pre 始终指向当前要交换的一对节点的前驱

        # 必须同时存在两个节点才需要交换
        while previous.next is not None and previous.next.next is not None:
            first = previous.next         # 这对的第一个节点
            second = previous.next.next   # 这对的第二个节点

            # 三步交换：1→second.next, 2→1, pre→2
            first.next = second.next      # 1 接上下一个对
            second.next = first           # 2 反指向 1
            previous.next = second        # pre 指向 2（现在这对的"头"）

            # pre 移到当前对的"第二个节点"（即 first），
            # 它将是下一对的前驱
            previous = first

        return dummy.next
