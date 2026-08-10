# LeetCode 39: 组合总和 (Combination Sum)
#
# 题目：给定一个无重复元素的数组 candidates 和一个目标数 target，
# 找出 candidates 中所有可以使数字和为 target 的组合。
# candidates 中的数字可以被无限次重复选取。
# 组合是无序的，解集不能包含重复的组合（例如 [2,2,3] 和 [3,2,2] 算同一个）。
#
# 核心思路（回溯 / DFS + "选或不选"模型）：
# 和 056 子集 类似，也是用 start_index 避免重复组合。
# 但有两个关键区别：
#   1. 元素可以无限次使用 → 选了之后下次还可以从当前位置开始（不是 i+1）
#   2. 有目标和限制 → 多了 total 参数和剪枝条件
#
# "选或不选"的决策树（n = 3, candidates = [2, 3, 5], target = 8）：
#   每个节点有两个分支：选当前的数（左，可以再选），跳过当前的数（右，去下一个）
#
#                    i=0, total=0, []
#                   /                    \
#          选2(留i=0)                   跳过2(i=1)
#         i=0,total=2,[2]              i=1,total=0,[]
#         /           \                  /           \
#    再选2          跳过2             选3          跳过3
#   i=0,t=4,[2,2]  i=1,t=2,[2]    i=1,t=3,[3]   i=2,t=0,[]
#     /     \         /     \         /     \        /     \
#   再选2    跳过    选3   跳过      选3   跳过    选5    跳过
#  t=6,[2,2,2]  ...  ...   ...    t=6,[3,3] ...  ...    ...
#   /     \
# 再选2    跳过
# t=8,[2,2,2,2] → 收集！✓ (total=8)
#
#   在这个过程中，路径不能回头（i 只增不减），所以不会出现 [2,3,3] 和 [3,2,3] 这种重复。
#   但选了当前数之后 i 不变，所以同一个数可以被反复选。
#
# 另一种等价的写法（for + start_index，和 056 子集更接近）：
#   def backtrack(start, current, total):
#       if total == target: result.append(current[:]); return
#       if total > target: return
#       for i in range(start, len(candidates)):
#           current.append(candidates[i])
#           backtrack(i, current, total + candidates[i])  # 还从 i 开始（可重复选）
#           current.pop()
#
# 时间复杂度：O(n^(target/min)) —— 最坏情况，每个都是1，选到 target 层
# 空间复杂度：O(target/min)——递归栈深度

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]   # 组合列表，每个组合的和 == target
        """
        result = []

        def dfs(i, current, total):
            """
            DFS "选或不选" 模型：
            i       —— 当前考虑 candidates 中第 i 个元素
            current —— 当前已选中的数字列表
            total   —— 当前已选数字的总和
            """
            # 找到目标和 → 收集结果（注意复制一份）
            if total == target:
                result.append(current.copy())
                return

            # 越界 / 和超了 → 剪枝，不再往下走
            if i >= len(candidates) or total > target:
                return

            # === 分支1：选当前的数（i 不变，因为可以重复选！）===
            current.append(candidates[i])
            dfs(i, current, total + candidates[i])    # 还是传 i，允许重复
            current.pop()   # 撤销选择

            # === 分支2：跳过当前的数，去下一个 ===
            dfs(i + 1, current, total)

        dfs(0, [], 0)
        return result
