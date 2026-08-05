# LeetCode 199: 二叉树的右视图 (Binary Tree Right Side View)
#
# 题目：站在二叉树的右侧，从上到下能看到哪些节点。
# 换句话说，每层的最右边那个节点。
#
# 核心思路（BFS 层序遍历，取每层最后一个节点）：
# 就是 041 层序遍历的变体——同一套 BFS + 队列框架，
# 只是每轮不再收集整层，而只记录该层最后一个节点。
#
# 例如：
#       1          ← 右视图看第1层：最右是 1
#      / \
#     2   3        ← 右视图看第2层：最右是 3
#      \   \
#       5   4      ← 右视图看第3层：最右是 4
#      /
#     6            ← 右视图看第4层：最右是 6
#   输出：[1, 3, 4, 6]
#
# 时间复杂度：O(n)——每个节点入队一次、出队一次
# 空间复杂度：O(n)——队列最多存一整层的节点

from collections import deque

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode | None
        :rtype: List[int]   # 从右视图看到的节点值，从上到下
        """
        if root is None:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)  # 当前层的节点数

            # 遍历当前层的每个节点
            for index in range(level_size):
                node = queue.popleft()

                # 关键：当前层的最后一个节点 = 右视图能看到的节点
                if index == level_size - 1:
                    result.append(node.val)

                # 左右子节点入队，属于下一层
                # 注意顺序：先左后右，保证同一层从左到右排列
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

        return result
