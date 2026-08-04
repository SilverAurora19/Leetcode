# LeetCode 101: 对称二叉树 (Symmetric Tree)
#
# 核心思路（递归，双指针镜像比较）：
# 对称二叉树：根节点的左子树和右子树互为镜像。
# 两个子树互为镜像的条件：
#   1. 两棵子树的根节点值相等
#   2. 左子树的"左"和右子树的"右"镜像对称（外侧）
#   3. 左子树的"右"和右子树的"左"镜像对称（内侧）
#
# 例如：
#         1              镜像比较：
#        / \              ○ 外侧：left.left(3) vs right.right(3) ✓
#       /   \             ○ 内侧：left.right(4) vs right.left(4) ✓
#      2     2            ○ 值：2 == 2 ✓
#     / \   / \
#    3   4 4   3
#
# 不是对称的例子：
#         1
#        / \              2.left(3) vs 2.right(3)? 值相等但...
#       2   2             外侧：3 vs null → 不对称！
#      /     \
#     3       3
#
# 时间复杂度：O(n)——每个节点访问一次
# 空间复杂度：O(h)——h 为树高，递归调用栈深度

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode | None
        :rtype: bool
        """
        # 空树视为对称
        if root is None:
            return True

        # 转化为比较左子树和右子树是否互为镜像
        return self.isMirror(root.left, root.right)

    def isMirror(self, left_node, right_node):
        """判断两棵子树是否互为镜像"""
        # 情况1：两边都为空 → 对称 ✓
        if left_node is None and right_node is None:
            return True

        # 情况2：只有一边为空 → 不对称 ✗
        if left_node is None or right_node is None:
            return False

        # 情况3：两边值不相等 → 不对称 ✗
        if left_node.val != right_node.val:
            return False

        # 情况4：值相等 → 递归比较子树
        # 外侧：左子树的左 vs 右子树的右（最外圈的节点）
        outer_same = self.isMirror(left_node.left, right_node.right)
        # 内侧：左子树的右 vs 右子树的左（靠中间的两个节点）
        inner_same = self.isMirror(left_node.right, right_node.left)

        # 外侧和内侧都对称才算对称
        return outer_same and inner_same
