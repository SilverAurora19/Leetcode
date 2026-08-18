# LeetCode 121: 买卖股票的最佳时机 (Best Time to Buy and Sell Stock)
#
# 题目：给定每天的股价，只允许买卖一次（先买后卖），求最大利润。
# 如果怎么买都亏，返回 0。
#
# 核心思路（一次遍历，动态维护最低买入价）：
# 遍历每一天，同时维护两个变量：
#   - min_price：到目前为止看到的最低股价（最佳买入点）
#   - max_profit：到目前为止能获得的最大利润
#
# 对每一天：
#   1. 更新 min_price（今天的价格是否更便宜？）
#   2. 计算"如果今天卖出"的利润 = 当前价格 - min_price
#   3. 更新 max_profit
#
# 为什么这样就是对的？
#   最大利润一定 = 某天的价格 - 那天之前的最低价格。
#   遍历时 min_price 恰好维护了"截至今天的最低价格"，
#   所以每天用 当前价 - min_price 就能算出"以今天为卖出日的最大利润"。
#
# 例如：prices = [7, 1, 5, 3, 6, 4]
#   第0天(7)：min_price=7, profit=0, max_profit=0
#   第1天(1)：min_price=min(1,7)=1, profit=1-1=0
#   第2天(5)：min_price=1, profit=5-1=4, max_profit=4
#   第3天(3)：min_price=1, profit=3-1=2
#   第4天(6)：min_price=1, profit=6-1=5, max_profit=5
#   第5天(4)：min_price=1, profit=4-1=3
#   返回 5（第1天买1，第4天卖6，赚5）
#
# 时间复杂度：O(n)
# 空间复杂度：O(1)

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]   # 每天的股价
        :rtype: int               # 最大利润
        """
        min_price = prices[0]   # 截至目前看到的最低价格（假设第一天买入）
        max_profit = 0          # 最大利润，初始为 0（允许不交易）

        for price in prices:
            # 1. 更新最低买入价
            min_price = min(price, min_price)

            # 2. 计算"今天卖出"的利润
            profit = price - min_price

            # 3. 更新最大利润
            max_profit = max(profit, max_profit)

        return max_profit
