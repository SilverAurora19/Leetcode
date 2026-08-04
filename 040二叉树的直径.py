# LeetCode 543: 二叉树的直径 (Diameter of Binary Tree)
#
# 直径定义：树中任意两个节点之间最长路径的长度（经过的边数）。
# 注意：直径不一定经过根节点！
#
# 核心思路（递归 DFS，计算深度的同时更新直径）：
# 经过某个节点的"最长路径" = 左子树深度 + 右子树深度。
# 因为穿过该节点的最长路径就是：左子树最深的叶子 → 当前节点 → 右子树最深的叶子。
#
# 所以我们先递归求左右子树的深度，顺手把 "左深+右深" 和全局最大直径比较，
# 然后向上返回当前节点深度 = max(左深, 右深) + 1（同样是求最大深度！）。
#
# 例如：
#        1
#       / \
#      2   3
#     / \
#    4   5
#
#   叶子 4：左右空 → 深=1, 经过 4 的直径=0+0=0
#   叶子 5：左右空 → 深=1, 经过 5 的直径=0+0=0
#   节点 2：左深=1, 右深=1 → 经过 2 的直径=1+1=2, 深=max(1,1)+1=2
#   叶子 3：左右空 → 深=1, 经过 3 的直径=0+0=0
#   根 1：  左深=2, 右深=1 → 经过 1 的直径=2+1=3, 深=max(2,1)+1=3
#
#   全局最大直径 = max(0, 0, 2, 0, 3) = 3（路径：4→2→1→3 或 5→2→1→3）
#
# 时间复杂度：O(n)——每个节点访问一次
# 空间复杂度：O(h)——h 为树高，递归调用栈深度

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode | None
        :rtype: int   # 树的直径（最长路径的边数）
        """
        self.max_diameter = 0   # 全局最大直径，递归过程中不断更新

        def depth(node):
            """
            返回以 node 为根的树的最大深度，
            同时顺手更新"经过 node 的直径"到 self.max_diameter。
            """
            if node is None:
                return 0

            # 先递归求左右子树深度（自底向上）
            left_depth = depth(node.left)
            right_depth = depth(node.right)

            # 经过当前节点的路径长度 = 左深 + 右深
            # （左边最深叶子 → 当前节点 → 右边最深叶子 的边数）
            current_diameter = left_depth + right_depth

            # 更新全局最大直径
            self.max_diameter = max(self.max_diameter, current_diameter)

            # 向上返回当前节点的深度，给上一层用（同二叉树最大深度 037）
            return max(left_depth, right_depth) + 1

        depth(root)
        return self.max_diameter
