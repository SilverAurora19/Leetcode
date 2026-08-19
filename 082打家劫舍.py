# LeetCode 198: 打家劫舍 (House Robber)
#
# 题目：一排房子，每家有金额。不能偷相邻的两家，问最多能偷多少钱。
#
# 核心思路（动态规划 + 滚动变量）：
# 走到第 i 家，只有两种选择：
#   1. 偷第 i 家 → 就不能偷第 i-1 家，收益 = 偷到第 i-2 家的最大值 + nums[i]
#   2. 不偷第 i 家 → 收益 = 偷到第 i-1 家的最大值
# 取两者较大值。
#
# 状态定义：
#   rob1 = 偷到"前两家"为止的最大金额（i-2）
#   rob2 = 偷到"前一家"为止的最大金额（i-1）
#
# 递推：temp = max(rob1 + n, rob2)
#       然后滚动：rob1 变成旧的 rob2，rob2 变成 temp
#
# 例如：nums = [2, 7, 9, 3, 1]
#   初始：rob1=0, rob2=0
#   n=2：temp=max(0+2, 0)=2；rob1=0, rob2=2
#   n=7：temp=max(0+7, 2)=7；rob1=2, rob2=7
#   n=9：temp=max(2+9, 7)=11；rob1=7, rob2=11
#   n=3：temp=max(7+3, 11)=11；rob1=11, rob2=11
#   n=1：temp=max(11+1, 11)=12；rob1=11, rob2=12
#   返回 12（偷 2、9、1 = 12，跳过了 7 和 3）
#
# 时间复杂度：O(n)
# 空间复杂度：O(1)——只用两个变量，不需要 dp 数组

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]   # 每家的金额
        :rtype: int             # 最多能偷到的金额
        """
        rob1, rob2 = 0, 0   # rob1=前两家最大值, rob2=前一家最大值

        for n in nums:
            # 偷当前家（rob1 + n）还是跳过当前家（rob2），取较大
            temp = max(rob1 + n, rob2)

            # 滚动更新：前一家变成前两家，当前变成前一家
            rob1 = rob2
            rob2 = temp

        return rob2   # 循环结束 rob2 就是全局最大值
