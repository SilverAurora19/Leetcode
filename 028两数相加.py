# LeetCode 2: 两数相加 (Add Two Numbers)
# 题目：两个逆序链表表示两个数（个位→十位→百位→...），返回它们的和（同样逆序）。
#
# 核心思路（模拟竖式加法）：
# 同时遍历两个链表，逐位相加并处理进位，就像手算加法一样。
# dummy + tail 模式构建结果链表（同 027）。
#
# 例如：l1 = 2→4→3（表示 342），l2 = 5→6→4（表示 465）
#   个位：2+5=7, carry=0 → 7
#   十位：4+6=10, carry=1 → 0
#   百位：3+4+1=8, carry=0 → 8
#   结果：7→0→8（表示 807 = 342 + 465）
#
# 时间复杂度：O(max(m, n))
# 空间复杂度：O(max(m, n))（结果链表的长度）

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode | None
        :type l2: ListNode | None
        :rtype: ListNode | None   # 和的逆序链表
        """
        dummy = ListNode(0)   # 虚拟头节点（值随意，只用作占位）
        tail = dummy           # tail 始终指向结果链的最后一个节点

        carry = 0              # 进位（0 或 1）

        # 只要还有节点未处理，或还有未清零的进位，就继续循环
        while l1 is not None or l2 is not None or carry != 0:
            # 取当前位的值，如果某链表已空则视为 0
            value1 = l1.val if l1 is not None else 0
            value2 = l2.val if l2 is not None else 0

            total = value1 + value2 + carry   # 当前位和

            digit = total % 10                 # 这位的结果（个位）
            carry = total // 10                # 进位（十位部分）

            # 把这位的结果接到结果链末尾
            tail.next = ListNode(digit)
            tail = tail.next

            # 两链表指针各自前进（如果还没走完）
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return dummy.next  # 跳过虚拟头，返回真正的结果头
