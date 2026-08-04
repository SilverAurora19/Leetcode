# LeetCode 102: 二叉树的层序遍历 (Binary Tree Level Order Traversal)
#
# 题目要求：一层一层地输出节点的值，每层一个子列表。
# 例如：
#       3
#      / \
#     9  20
#        / \
#       15  7
#   输出：[[3], [9,20], [15,7]]
#
# 核心思路（BFS + 队列）：
# 用队列（queue，先进先出）逐层处理。
# 每轮先数一下当前队列的长度 level_size，这就是"当前层有几个节点"；
# 然后恰好处理 level_size 个节点，同时把它们的子节点加入队列。
#
# 为什么用队列而不是栈？
#   队列先进先出，保证同一层的节点按从左到右的顺序被处理；
#   栈后进先出，会变成深度优先搜索（先一路扎到底）。
#
# 时间复杂度：O(n)——每个节点入队一次、出队一次
# 空间复杂度：O(n)——队列最多存一整层的节点（最底层约 n/2 个）

from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode | None
        :rtype: List[List[int]]   # 二维列表，每个子列表是一层的值
        """
        if root is None:
            return []

        result = []
        queue = deque([root])    # 队列，初始化放入根节点

        while queue:
            # 当前队列中的节点数 = 当前层的节点数（关键！）
            level_size = len(queue)
            current_level = []    # 存放当前层的值

            # 恰好处理 level_size 个节点，不多不少
            for _ in range(level_size):
                node = queue.popleft()          # 从队头取出一个节点（FIFO）
                current_level.append(node.val)  # 记录该节点的值

                # 把左右子节点加入队尾，它们属于下一层
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            # 当前层处理完毕，加入结果
            result.append(current_level)

        return result
