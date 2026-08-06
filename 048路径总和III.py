# LeetCode 437: 路径总和 III (Path Sum III)
#
# 题目：找出二叉树中所有路径和为 targetSum 的路径数。
# 路径必须从上到下（父→子方向），但不一定要从根开始，也不一定要在叶子结束。
#
# 核心思路（前缀和 + 哈希表 + DFS 回溯）：
# 这道题本质是 010 和为 K 的子数组"搬到了树上"。
#
# 回顾 010：在数组里，如果 current_sum - targetSum 出现过 n 次，
#          就说明有 n 个子数组以当前位置结尾且和为 targetSum。
#
# 在树上同理：从根到当前节点，这是一条"路径"，相当于数组。
#   prefix_count 记录这条路径上每个前缀和出现了几次。
#   当前前缀和 - targetSum 出现过几次 = 以当前节点结尾的合法路径数。
#
# 区别在于树有分支：进入子树前要把当前前缀和记入 prefix_count，
# 离开子树后要减回去（回溯），否则会在不该出现的地方被统计到。
#
# 例如：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
#
#   路径：10 → 5 → 3
#   前缀和：10, 15, 18
#   在节点 3：current_sum=18, need=18-8=10 → prefix_count[10]=1 → 有1条路径（5→3=8）
#
# 时间复杂度：O(n)——每个节点访问一次
# 空间复杂度：O(h)——哈希表最多存 h 个前缀和（一条路径的深度）

class Solution:
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode | None
        :type targetSum: int
        :rtype: int   # 路径和为 targetSum 的路径总数
        """
        self.answer = 0

        # 前缀和 → 出现次数
        # 前缀和为 0 初始出现 1 次，处理"路径从根开始"的情况
        prefix_count = {0: 1}

        def dfs(node, current_sum):
            """DFS 遍历树，维护从根到当前节点这条路径上的前缀和统计"""
            if node is None:
                return

            # 更新当前路径的前缀和
            current_sum += node.val

            # 查询：有多少历史前缀和 = current_sum - targetSum？
            # 有几个就说明有几条路径以当前节点结尾且和为 targetSum
            need_sum = current_sum - targetSum
            self.answer += prefix_count.get(need_sum, 0)

            # 将当前前缀和记入哈希表（为孙子节点使用）
            prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

            # 向左右子树深入
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)

            # 回溯！离开当前节点时要把它的前缀和移除，
            # 否则兄弟子树的路径会错误地用上不属于它的前缀和
            prefix_count[current_sum] -= 1

        dfs(root, 0)
        return self.answer
