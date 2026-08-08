# 核心思路（前缀积 × 后缀积）：
# 要求：返回 answer[i] = nums 中除 nums[i] 之外所有元素的乘积（不能用除法）。
#
# 以 nums = [2, 3, 4, 5] 为例：
#   answer[2] = 左边元素的乘积 × 右边元素的乘积
#             = (2 × 3)      × (5)
#             = 前缀积        × 后缀积
#
# 两次遍历：
#   第1趟（左→右）：answer[i] 暂存 nums[i] 左侧所有元素的乘积
#   第2趟（右→左）：answer[i] 再乘上 nums[i] 右侧所有元素的乘积
#
# 时间复杂度：O(n)
# 空间复杂度：O(1)（输出数组不计入额外空间）
# 每个位置的答案等于左侧乘积乘右侧乘积；先从左往右存左积，再从右往左乘右积。

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]   # 整数数组
        :rtype: List[int]       # answer[i] = 除 nums[i] 外所有元素的乘积
        """
        n = len(nums)
        answer = [1] * n  # 初始化全为 1，作为累积乘积的起点

        # ---- 第1趟：从左到右，计算前缀积 ----
        left_product = 1  # 累积 nums[i] 左侧所有元素的乘积
        for index in range(n):
            answer[index] = left_product       # 此时 answer[i] = nums[0] × ... × nums[i-1]
            left_product *= nums[index]        # 把当前元素乘入 left_product，供下一位使用

        # ---- 第2趟：从右到左，乘上后缀积 ----
        right_product = 1  # 累积 nums[i] 右侧所有元素的乘积
        for index in range(n - 1, -1, -1):     # 从最后一个元素往前遍历
            answer[index] *= right_product     # answer[i] = 前缀积 × 后缀积
            right_product *= nums[index]       # 把当前元素乘入 right_product

        return answer
