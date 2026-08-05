# LeetCode 108: 将有序数组转换为二叉搜索树 (Convert Sorted Array to BST)
#
# 二叉搜索树（BST）的性质：
#   左子树所有节点 < 根 < 右子树所有节点
#   中序遍历结果 = 升序排列
#
# 核心思路（递归 + 二分）：
# 题目要求构造一棵"高度平衡"的 BST，即左右子树高度差不超过 1。
# 既然数组已经有序，那就每次都取正中间的元素作为根：
#   - 中间元素左边的数组 → 递归构造左子树
#   - 中间元素右边的数组 → 递归构造右子树
# 这样左右子树节点数最大差 1，天然平衡。
#
# 例如：nums = [-10, -3, 0, 5, 9]
#                     ↑ mid
#           根 = 0
#          /      \
#   [-10, -3]    [5, 9]
#      ↑ mid      ↑ mid
#    根 = -3     根 = 9
#    /    \       /
#  [-10]  []   [5]
#    ↑          ↑
#   根 = -10   根 = 5
#
#   结果：    0
#           / \
#         -3   9
#         /   /
#       -10  5
#
# 时间复杂度：O(n)——每个元素访问一次
# 空间复杂度：O(log n)——递归调用栈深度 = 树的高度

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]        # 升序排列的整数数组
        :rtype: TreeNode | None      # 高度平衡的 BST 根节点
        """

        def build(left, right):
            """递归构造 nums[left..right] 区间对应的平衡 BST"""
            # 区间不合法（空区间）→ 返回 None，表示空子树
            if left > right:
                return None

            # 取区间中点作为当前子树的根（保证左右节点数均衡）
            middle = (left + right) // 2
            root = TreeNode(nums[middle])    # 用中间值创建节点

            # 递归构造左右子树
            root.left = build(left, middle - 1)      # 左半区：left ~ middle-1
            root.right = build(middle + 1, right)     # 右半区：middle+1 ~ right

            return root

        return build(0, len(nums) - 1)  # 从整个数组开始建树
