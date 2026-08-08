# LeetCode 236: 二叉树的最近公共祖先 (Lowest Common Ancestor of a Binary Tree)
#
# 题目：给定一棵二叉树和两个节点 p、q，找到 p 和 q 的最近公共祖先（LCA）。
# LCA 定义：在 p 和 q 的所有公共祖先中，深度最深的那个节点。
# 一个节点也可以是它自己的祖先（即 LCA 可以是 p 或 q 本身）。
#
# 核心思路（递归，自底向上）：
# 这道题本质是一个"后序遍历"——先查左右子树，再根据左右结果判断当前节点。
#
# 递归函数定义：返回以当前节点为根的子树中，p 或 q 的"出现情况"。
#   - 如果子树中包含 p 或 q，返回该节点（p 或 q 本身）
#   - 如果子树中同时包含 p 和 q，返回它们的 LCA
#   - 如果什么都没找到，返回 None
#
# 判断逻辑（在每一层）：
# 1. 如果当前节点是 p 或 q，或者当前节点为空 → 直接返回当前节点（递归出口）
# 2. 递归查左子树 → left，递归查右子树 → right
# 3. 如果 left 和 right 都不为空：
#    → 说明 p 和 q 分别位于当前节点的左右两侧
#    → 当前节点就是 LCA！（这是唯一的分叉点）
# 4. 如果只有一侧不为空：
#    → 说明 p 和 q 都在那一侧子树中（或者已经找到了 LCA）
#    → 把那个非空结果"往上传递"
#
# 为什么对？因为 LCA 是唯一一个满足"p 和 q 分别在左右子树"的节点。
# 在这个节点之上，左右子树之一会是空的（另一个包含 LCA 本身），
# 那个非空结果会一直被传递到最顶层。
#
# 例如：root = [3,5,1,6,2,0,8,null,null,7,4], p=5, q=1
#
#          3
#        /   \
#       5     1
#      / \   / \
#     6   2 0   8
#        / \
#       7   4
#
#   从底向上：
#   节点 6：left=None right=None, 6不是p/q → 返回 None
#   节点 7：7不是p/q → 返回 None
#   节点 4：4不是p/q → 返回 None
#   节点 2：left=7(→None), right=4(→None), 2不是p/q → 返回 None
#   节点 5：left=6(→None), right=2(→None), 但 5==p → 返回 5
#   节点 0：0不是p/q → 返回 None
#   节点 8：8不是p/q → 返回 None
#   节点 1：left=0(→None), right=8(→None), 但 1==q → 返回 1
#   节点 3：left=5(来自p), right=1(来自q) → 两边都不空！→ 3 就是 LCA ✓
#
# 另一个例子：p=5, q=4（p 是 q 的祖先）
#
#   节点 4：4==q → 返回 4
#   节点 2：left=7(→None), right=4(q) → 一侧非空，返回 4（往上传递）
#   节点 5：left=6(→None), right=2(→4), 且 5==p → 返回 5（自己是p，直接返回）
#   节点 3：left=5(p), right=1(→None) → 一侧非空，返回 5 ← 答案
#   注意：节点 2 的 right=4 并没有机会和 5 汇合，因为 5 已经在它上面直接返回了。
#   这正是我们想要的行为——p 本身就是 q 的祖先，所以 LCA 就是 p。
#
# 时间复杂度：O(n)——每个节点最多访问一次
# 空间复杂度：O(h)——递归调用栈深度，h 为树高

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode | None
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode | None   # p 和 q 的最近公共祖先
        """
        # 递归出口：空节点 / 遇到 p 或 q → 直接返回
        # "遇到 p 或 q 就返回"的含义是：这个子树至少包含 p 或 q 之一
        if root is None or root is p or root is q:
            return root

        # 后序遍历：先查左右子树
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 情况1：左右都不为空 → p 和 q 分别在当前节点的两侧
        #         当前节点就是 LCA（分叉点），返回它
        if left and right:
            return root

        # 情况2：只有一侧不为空 → p 和 q 都在那一侧（或已经找到 LCA）
        #         把非空结果"往上传递"
        if left is not None:
            return left
        return right
