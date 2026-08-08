# LeetCode 104: 二叉树的最大深度 (Maximum Depth of Binary Tree)
#
# 核心思路（递归，自底向上）：
# 一棵树的最大深度 = max(左子树深度, 右子树深度) + 1（当前节点这一层）。
# 递归到底（遇到空节点）返回 0，然后逐层往上累加。
#
# 例如：
#       3             ← 深度 = max(2, 1) + 1 = 3
#      / \
#     9  20           ← 左深度=1, 右深度 = max(1, 1) + 1 = 2
#        / \
#       15  7         ← 左右各深度=1
#
# 递归过程：
#   叶子节点 9：左右都为空 → max(0,0)+1 = 1
#   叶子节点 15：max(0,0)+1 = 1
#   叶子节点 7：max(0,0)+1 = 1
#   节点 20：max(1,1)+1 = 2
#   根节点 3：max(1,2)+1 = 3 ← 答案
#
# 时间复杂度：O(n)——每个节点访问一次
# 空间复杂度：O(h)——h 为树高，递归调用栈深度

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode | None
        :rtype: int   # 树的最大深度
        """
        # 空节点深度为 0，也是递归的终止条件
        if root is None:
            return 0

        # 递归求左右子树的深度
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # 当前节点的深度 = 较深的那棵子树深度 + 1（自己这层）
        return max(left_depth, right_depth) + 1
