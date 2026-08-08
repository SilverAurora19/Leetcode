# LeetCode 234: 回文链表 (Palindrome Linked List)
#
# 核心思路（快慢指针找中点 + 反转后半段 + 从两边同时向中间比较）：
#
# 例如：1 → 2 → 2 → 1 → None
#   1. 快慢指针找中点 → 慢指针停在第一个 2（前半段末尾）
#   2. 反转后半段     → 1 → 2 → null ← 2 ← 1
#   3. 头尾同时比较   → 1==1 ✓, 2==2 ✓，回文！
#
# 时间复杂度：O(n)
# 空间复杂度：O(1)

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode | None
        :rtype: bool
        """
        # 空链表或单节点一定是回文
        if head is None or head.next is None:
            return True

        # 第1步：快慢指针找到前半段的末尾（慢指针）
        first_half_end = self.findFirstHalfEnd(head)

        # 第2步：反转后半段链表，返回新头
        second_half_start = self.reverseList(first_half_end.next)

        # 第3步：从头部和反转后的后半段头同时比较
        left_pointer = head                
        right_pointer = second_half_start
        is_palindrome = True

        # 后半段长度 ≤ 前半段长度，所以只要 right_pointer 没走完就继续比较
        while right_pointer is not None:
            if left_pointer.val != right_pointer.val:
                is_palindrome = False
                break

            left_pointer = left_pointer.next
            right_pointer = right_pointer.next

        # 恢复原链表结构：把反转过的后半段再反转回去并接上
        first_half_end.next = self.reverseList(second_half_start)

        return is_palindrome

    def findFirstHalfEnd(self, head):
        """快慢指针找前半段末尾：慢指针每次走一步，快指针走两步。
           快指针到达末尾时，慢指针正好在前半段最后一个节点。
           例：1→2→2→1 → 返回节点 2（第一个2）
           例：1→2→3→2→1 → 返回节点 2（中间节点前一个）"""
        slow = head
        fast = head

        # 快指针两步两步走，慢指针一步步跟
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverseList(self, head):
        """反转链表（迭代），返回新头"""
        previous = None
        current = head

        while current is not None:
            next_node = current.next      # 暂存下一个
            current.next = previous       # 反转指向
            previous = current            # prev 前移
            current = next_node           # curr 前移

        return previous
