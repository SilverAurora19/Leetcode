# LeetCode 206: 反转链表 (Reverse Linked List)
#
# 核心思路（迭代，三指针）：
# 用 prev / curr / next 三个指针，逐个翻转节点的指向：
#   1. 先保存 curr.next（否则断了就找不到了）
#   2. 把 curr.next 指向 prev（反转）
#   3. prev 和 curr 都前进一步
#
# 初始时 prev = None（反转后原头节点指向 None，成为新尾节点）。
#
# 例如：1 → 2 → 3 → None
#   prev=null, curr=1  →  1 → null, prev=1, curr=2
#                     →  2 → 1 → null, prev=2, curr=3
#                     →  3 → 2 → 1 → null, prev=3, curr=None（退出）
#   返回 prev = 3（新头节点）
#
# 时间复杂度：O(n)
# 空间复杂度：O(1)

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode | None
        :rtype: ListNode | None   # 反转后的新头节点
        """
        previous = None    # 已翻转部分的新头（随着推进最终成为整个新链表的头）
        current = head     # 当前正在处理的节点

        while current is not None:
            next_node = current.next    # 1. 暂存下一个节点，防止断链
            current.next = previous     # 2. 反转：当前节点指向前一个节点
            previous = current          # 3. prev 前移
            current = next_node         # 4. curr 前移（用之前暂存的 next_node）

        # 循环结束后 prev 指向原链表的最后一个节点，即新链表的头
        return previous
