# LeetCode 114: 二叉树展开为链表 (Flatten Binary Tree to Linked List)
#
# 题目要求：原地将二叉树展开成一个"只有右子树"的链表，顺序按前序遍历。
#   每个节点的 left 置为 None，right 指向下一个节点。
#
# 核心思路（栈 + 前序遍历 + 逐个串联）：
# 用栈做前序遍历（根→左→右），同时用 previous 指针记录上一个访问的节点。
# 每弹出一个节点，就把 previous 的 left 置空、right 指向当前节点。
#
# 注意：压栈顺序是"先右后左"——因为栈是后进先出，这样才能先处理左子树。
#
# 例如：
#       1           展开后：1 → 2 → 3 → 4 → 5 → 6 → None
#      / \
#     2   5
#    / \   \
#   3   4   6
#
# 步骤演算：
#   栈[1] → 弹1, pre=None, 压5压2 → 栈[5,2]
#   弹2, pre=1→1.right=2, pre.left=null, 压4压3 → 栈[5,4,3]
#   弹3, pre=2→2.right=3, 3无子 → 栈[5,4]
#   弹4, pre=3→3.right=4 → 栈[5]
#   弹5, pre=4→4.right=5, 压6 → 栈[6]
#   弹6, pre=5→5.right=6 → 栈[]
#   结果：1→2→3→4→5→6→None
#
# 时间复杂度：O(n)——每个节点入栈一次、出栈一次
# 空间复杂度：O(h)——栈中最多存 h 个节点

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode | None
        :rtype: None   # 原地修改，不返回
        """
        if root is None:
            return

        stack = [root]        # 前序遍历用的栈，初始压入根
        previous = None       # 上一个被访问的节点（用于串联链表）

        while stack:
            current = stack.pop()   # 弹出栈顶，当前访问的节点

            # 保证先左后右：先压右、再压左（左后进，先出栈）
            if current.right is not None:
                stack.append(current.right)
            if current.left is not None:
                stack.append(current.left)

            # 把上一个节点和当前节点串联起来
            if previous is not None:
                previous.left = None       # left 指针置空
                previous.right = current   # right 指向下一个节点

            # 当前节点变为"上一个"，准备下一轮串联
            previous = current
