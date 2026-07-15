# 核心思路（排序 + 双指针）：
# 题目：从 nums 中找出所有和为 0 且不重复的三元组。
#
# 1. 先对数组从小到大排序，方便跳过重复值和控制指针移动方向。
# 2. 固定第一个数 first，在它右侧的区间用 left/right 双指针找另外两个数：
#    - 三数和 > 0 → right 左移（需要更小的数）
#    - 三数和 < 0 → left 右移（需要更大的数）
#    - 三数和 = 0 → 找到一组解，同时移动左右指针并跳过重复值
# 3. 去重贯穿始终：固定的 first、left、right 都要跳过连续相同的值。
#
# 时间复杂度：O(n²)——外层遍历 O(n)，内层双指针 O(n)
# 空间复杂度：O(1)——不计结果数组

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]   # 返回所有和为 0 且不重复的三元组
        """
        nums.sort()  # 从小到大排序，是双指针和去重的前提
        result = []
        n = len(nums)

        # 固定第一个数，只需遍历到倒数第3个（后面至少留两个给 left 和 right）
        for first in range(n - 2):
            # 排序后如果第一个数已经 > 0，后面全正，不可能再和为 0
            if nums[first] > 0:
                break
            # 跳过重复的 first（与上一个 first 值相同则跳过）
            if first > 0 and nums[first] == nums[first - 1]:
                continue

            left = first + 1       # 左指针从 first 右侧开始
            right = n - 1          # 右指针从数组末尾开始

            while left < right:
                total = nums[first] + nums[left] + nums[right]

                if total > 0:
                    right -= 1     # 和偏大 → 右指针左移，让和变小
                elif total < 0:
                    left += 1      # 和偏小 → 左指针右移，让和变大
                else:
                    # 找到一组解
                    result.append([nums[first], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # 跳过左侧重复值（当前 left 与上一个 left 相同则跳过）
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # 跳过右侧重复值（当前 right 与下一个 right 相同则跳过）
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result
