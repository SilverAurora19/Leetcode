# LeetCode 230: 二叉搜索树中第 K 小的元素 (Kth Smallest Element in a BST)
#
# 核心思路（中序遍历 + 计数）：
# BST 的中序遍历结果 = 升序排列！
# 所以中序遍历到第 K 个节点就是答案，直接返回，不必遍历整棵树。
#
# 沿用 036 的迭代中序遍历（栈），只需加一个 k 计数器：
#   每弹出一个节点，k 减 1；k 归零时当前节点就是第 K 小的。
#
# 例如：     5
#           / \
#          3   6
#         / \
#        2   4
#       /
#      1
#   k=3，中序遍历顺序：1 → 2 → 3 ✓（弹出 3 时 k=0，返回 3）
#
# 时间复杂度：O(H + k)——H 为树高，最多走到第 k 个就停了
# 空间复杂度：O(H)——栈中最多存 H 个节点

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int   # 第 k 小的元素值
        """
        stack = []       # 模拟递归调用栈
        current = root   # 当前遍历指针

        # 经典迭代中序遍历（同 036），只是访问节点时计数
        while current is not None or stack:
            # 沿左子树一路走到底，所有经过的节点压栈
            while current is not None:
                stack.append(current)
                current = current.left

            # 左边到头，弹出栈顶访问（此时 current 是当前最小的未访问节点）
            current = stack.pop()

            k -= 1               # 每访问一个节点，k 减 1
            if k == 0:           # 正好第 k 个 → 这就是答案！
                return current.val

            # 转向右子树继续
            current = current.right

        return None  # 理论上不会走到这里（题目保证 k ≤ 节点数）
