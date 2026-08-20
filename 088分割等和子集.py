# LeetCode 416: 分割等和子集 (Partition Equal Subset Sum)
#
# 题目：判断数组能否分成两个子集，使它们的和相等。
# 即：能否选一些数，使它们的和 = 总和的一半。
#
# 核心思路（0/1 背包问题）：
# 转化为背包问题：有一个容量为 total/2 的背包，每个数只能用一次，
# 问能否恰好装满。
#
# dp[j] = 能否用某些数凑出和为 j。
#   初始 dp[0] = True（凑 0 不需要任何数）
#
# 对每个数 num，更新 dp：
#   dp[j] = dp[j] or dp[j - num]
#   即：不用 num 也能凑 j（dp[j]），或者用了 num 后能凑 j-num（dp[j-num]）
#
# 关键：内层循环必须"从大到小"（倒序遍历）！
#   如果正序遍历，同一个 num 可能被重复使用多次（变成完全背包），
#   而这里每个数只能用一次（0/1 背包）。
#
# 例如：nums = [1, 5, 11, 5]
#   total = 22，target = 11
#   初始 dp[0] = True
#   处理 1：dp[1] = True
#   处理 5：dp[5]=True, dp[6]=True
#   处理 11：dp[11]=True → 找到！返回 True（11 = 11，剩下 1+5+5 = 11）
#
# 时间复杂度：O(n × target)
# 空间复杂度：O(target)——一维 dp 数组

class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool   # 能否等和分割
        """
        total = sum(nums)

        # 总和是奇数 → 不可能分成两个相等的部分
        if total % 2 != 0:
            return False

        target = total // 2   # 目标：凑出总和的一半

        # dp[j] = 能否凑出和为 j
        dp = [False] * (target + 1)
        dp[0] = True           # 凑 0 一定可以（空子集）

        for num in nums:
            # 倒序遍历！保证每个 num 只用一次（0/1 背包）
            for j in range(target, num - 1, -1):
                # 不用 num 或 用了 num（需要 dp[j-num] 为 True）
                dp[j] = dp[j] or dp[j - num]

        return dp[target]
