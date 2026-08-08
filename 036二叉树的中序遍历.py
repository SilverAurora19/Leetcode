# LeetCode 94: 二叉树的中序遍历 (Binary Tree Inorder Traversal)
#
# 树的三种遍历方式（记住口诀）：
#   前序：根 → 左 → 右 （Pre-order）
#   中序：左 → 根 → 右 （In-order）★ 本题
#   后序：左 → 右 → 根 （Post-order）
#
# "中序"的意思是"根在中间访问"——先访问左子树，再访问根，最后访问右子树。
# 二叉搜索树的中序遍历结果是一个有序序列，这是中序最重要的性质。

# 树节点的定义（题目提供，不用写）
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val        # 当前节点保存的值
#         self.left = left      # 左子节点（也是一棵树）
#         self.right = right    # 右子节点（也是一棵树）

class Solution(object):
    # ===== 方法1：递归 =====
    # 递归本质是系统帮我们维护"调用栈"。
    # 代码很简洁，但递归深度受限于调用栈大小，极端情况下（树退化成链表）可能栈溢出。
    #
    # 时间复杂度：O(n)——每个节点访问一次
    # 空间复杂度：O(h)——h 为树高，递归调用栈的深度
    def inorderTraversal_1(self, root):
        """
        :type root: TreeNode | None
        :rtype: List[int]
        """
        result = []

        def inorder(node):
            """递归中序遍历：左 → 根 → 右"""
            if node is None:
                return

            inorder(node.left)          # 1. 先访问左子树
            result.append(node.val)     # 2. 访问根（记录值）
            inorder(node.right)         # 3. 最后访问右子树

        inorder(root)
        return result

    # ===== 方法2：迭代（用栈模拟递归）=====
    # 手动维护一个栈来模拟递归过程，避免调用栈溢出。
    #
    # 思路：沿着左子树一路走到底，边走边把节点压栈；
    #       走到空后从栈顶弹出节点访问，然后转向它的右子树。
    #
    # 例如：
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    #
    #   过程：一路向左 → 栈[1,2,4] → 弹4访问 → 4无右 → 弹2访问 → 转2的右5
    #        → 一路向左 → 栈[1,5] → 弹5访问 → 5无右 → 弹1访问 → 转1的右3
    #        → 一路向左 → 栈[3] → 弹3访问 → 3无右 → 栈空，结束
    #   结果：[4, 2, 5, 1, 3]
    #
    # 时间复杂度：O(n)
    # 空间复杂度：O(h)——h 为树高，栈中最多存 h 个节点
    def inorderTraversal_2(self, root):
        """
        :type root: TreeNode | None
        :rtype: List[int]
        """
        result = []
        stack = []        # 手动维护的栈
        current = root     # 当前节点指针

        # 只要还有节点没访问完（栈不空 或 当前指针不为空）
        while current is not None or stack:
            # 沿着左子树一路走到底，把所有经过的节点压栈
            while current is not None:
                stack.append(current)       # 暂存当前节点（稍后才访问它本身）
                current = current.left      # 继续深入左子树

            # 左边到头了，弹出栈顶节点，访问它
            current = stack.pop()
            result.append(current.val)      # 中序：弹出来才访问（根）

            # 转向右子树，对它做同样的操作
            current = current.right

        return result
