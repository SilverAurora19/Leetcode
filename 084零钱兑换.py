# LeetCode 322: 零钱兑换 (Coin Change)
#
# 题目：给定不同面额的硬币和一个总金额 amount，求凑成该金额所需的最少硬币数。
# 如果无法凑成，返回 -1。
#
# 核心思路（动态规划，自底向上）：
# dp[i] = 凑成金额 i 所需的最少硬币数。
#
# 递推公式：
#   dp[i] = min(1 + dp[i - coin])  对于每个 coin ≤ i
#   即：凑 i 的最优解 = 先凑 i-coin（用 dp[i-coin] 枚），再加 1 枚 coin
#
# 初始：
#   dp[0] = 0（凑 0 元需要 0 枚）
#   其他 dp[i] = 无穷大（表示暂时无法凑成）
#
# 例如：coins = [1, 2, 5], amount = 11
#   dp[0] = 0
#   dp[1] = min(1+dp[0]) = 1
#   dp[2] = min(1+dp[1], 1+dp[0]) = min(2, 1) = 1
#   dp[5] = min(1+dp[4], 1+dp[3], 1+dp[0]) = 1（直接用 5）
#   ...
#   dp[11] = 3（5 + 5 + 1）
#
# 时间复杂度：O(amount × len(coins))
# 空间复杂度：O(amount)——dp 数组

class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]   # 硬币面额
        :type amount: int        # 目标金额
        :rtype: int              # 最少硬币数，凑不成返回 -1
        """
        # 金额为 0 或负数，不需要任何硬币
        if amount < 1:
            return 0

        # dp[i] = 凑成金额 i 的最少硬币数，初始为无穷大（表示不可达）
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0   # 凑 0 元需要 0 枚硬币

        # 从小到大计算每个金额的最少硬币数
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    # 用一枚 coin + 凑 i-coin 的最少硬币数
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        # 如果 dp[amount] 还是无穷大，说明凑不成，返回 -1
        return -1 if dp[amount] == float('inf') else dp[amount]
