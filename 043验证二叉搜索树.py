# LeetCode 98: 验证二叉搜索树 (Validate Binary Search Tree)
#
# 二叉搜索树（BST）的严格定义：
#   对于任意节点 node，其值必须满足 lower < node.val < upper。
#   注意：仅仅是"左 < 根 < 右"不够！必须整棵左子树的所有节点都小于根。
#
# 反例（很多人会漏掉的情况）：
#       5
#      / \
#     1   6
#        / \
#       3   7
#   节点 3 虽然小于父节点 6，但它在根 5 的右子树中，仍然小于 5，违反了 BST 性质！
#
# 核心思路（递归 + 上下界）：
# 给每个节点一个"合法范围" (lower, upper)：
#   - 根节点：范围是 (-∞, +∞)
#   - 左子节点：范围是 (父的 lower, 父的值)    ← 父值成为上界
#   - 右子节点：范围是 (父的值, 父的 upper)    ← 父值成为下界
#   不合法：node.val <= lower 或 node.val >= upper
#
# 初始用 None 代表正负无穷，方便处理边界。
#
# 时间复杂度：O(n)——每个节点访问一次
# 空间复杂度：O(h)——递归调用栈深度

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode | None
        :rtype: bool
        """

        def validate(node, lower, upper):
            """验证以 node 为根的子树是否是一棵合法的 BST，
            并满足 lower < 所有节点值 < upper。
            lower/upper 为 None 表示没有下界/上界（即 -∞ / +∞）"""
            # 空节点是合法的 BST
            if node is None:
                return True

            # 检查当前节点是否在合法范围内
            if lower is not None and node.val <= lower:
                return False
            if upper is not None and node.val >= upper:
                return False

            # 递归验证左子树：上界收紧为当前节点值
            left_is_valid = validate(node.left, lower, node.val)

            # 递归验证右子树：下界收紧为当前节点值
            right_is_valid = validate(node.right, node.val, upper)

            # 左右子树都合法才算合法
            return left_is_valid and right_is_valid

        # 从根节点开始，初始无上下界
        return validate(root, None, None)
