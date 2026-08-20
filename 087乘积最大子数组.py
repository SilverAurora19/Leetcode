# LeetCode 152: 乘积最大子数组 (Maximum Product Subarray)
#
# 题目：求数组中连续子数组的乘积最大值。
#
# 核心思路（动态规划，同时维护最大和最小）：
# 与 013 最大子数组之和不同，乘积问题有个关键难点：
#   负数 × 负数 = 正数！
#   一个"最小的负数乘积"乘上当前的负数，可能变成"最大的正数"。
#
# 所以必须同时维护两个状态：
#   max_pro = 以当前位置结尾的"最大乘积"
#   min_pro = 以当前位置结尾的"最小乘积"
#
# 对每个数 num，三种可能成为新 max_pro 的候选：
#   1. num 本身（另起炉灶，重新开始子数组）
#   2. 旧的 max_pro × num（接在前面最大乘积后面）
#   3. 旧的 min_pro × num（接在前面最小乘积后面，负负得正！）
# 取三者最大。
#
# 注意：必须用 old_max/old_min 保存旧值，
#   因为 max_pro 更新后不能影响 min_pro 的计算（它们要用同一轮的旧值）。
#
# 例如：nums = [2, 3, -2, 4]
#   num=2：max=2, min=2, res=2
#   num=3：max=max(3, 2*3, 2*3)=6, min=min(3,2*3,2*3)=3, res=6
#   num=-2：max=max(-2, 6*-2, 3*-2)=-2, min=min(-2,6*-2,3*-2)=-12, res=6
#   num=4：max=max(4, -2*4, -12*4)=4, min=min(4,-2*4,-12*4)=-48, res=6
#   返回 6（子数组 [2,3] 的乘积）
#
# 时间复杂度：O(n)
# 空间复杂度：O(1)

class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int   # 乘积最大的连续子数组的乘积
        """
        max_pro = nums[0]   # 以当前位置结尾的最大乘积
        min_pro = nums[0]   # 以当前位置结尾的最小乘积（为负负得正准备）
        res = nums[0]       # 全局最大乘积

        for num in nums[1:]:
            # 保存旧值，因为下面两行都要用"更新前"的 max/min
            old_max = max_pro
            old_min = min_pro

            # 新 max_pro = 三种候选的最大值（修：加入乘法！）
            max_pro = max(num, old_max * num, old_min * num)

            # 新 min_pro = 三种候选的最小值
            min_pro = min(num, old_max * num, old_min * num)

            # 更新全局最大值
            res = max(res, max_pro)

        return res
