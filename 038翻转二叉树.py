# LeetCode 226: 翻转二叉树 (Invert Binary Tree)
#
# 核心思路（递归，自底向上交换）：
# 翻转二叉树就是让每个节点的左右子树对调。
# 递归过程：
#   1. 先递归翻转左子树，得到翻转后的左子树
#   2. 再递归翻转右子树，得到翻转后的右子树
#   3. 把当前节点的 left 指向翻转后的右子树，right 指向翻转后的左子树
#
# 注意顺序：必须先把翻转后的子树保存到临时变量，
# 否则直接交换会导致引用丢失。
#
# 例如：
#       4                  4
#      / \                / \
#     2   7    ==>       7   2
#    / \ / \            / \ / \
#   1  3 6  9          9  6 3  1
#
# 递归过程（以节点 2 为例）：
#   翻转 2 的左子树(1) → 1
#   翻转 2 的右子树(3) → 3
#   交换：2.left=3, 2.right=1  →  2 的左右对调
#
# 时间复杂度：O(n)——每个节点访问一次
# 空间复杂度：O(h)——h 为树高，递归调用栈深度

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode | None
        :rtype: TreeNode | None   # 翻转后的树根
        """
        # 空节点直接返回，递归终止条件
        if root is None:
            return None

        # 先递归翻转左右子树（自底向上：叶子先完成交换，逐层往上）
        inverted_left = self.invertTree(root.left)    # 翻转后的左子树
        inverted_right = self.invertTree(root.right)  # 翻转后的右子树

        # 交换当前节点的左右子树
        root.left = inverted_right
        root.right = inverted_left

        return root
