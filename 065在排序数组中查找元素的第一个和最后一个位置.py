# LeetCode 34: 在排序数组中查找元素的第一个和最后一个位置
# (Find First and Last Position of Element in Sorted Array)
#
# 核心思路（两次二分查找找边界）：
# 调用同一个 lower_bound 函数两次：
#   - 找左边界：lower_bound(target)     → 第一个 ≥ target 的位置
#   - 找右边界：lower_bound(target + 1) - 1 → 第一个 > target 的位置减 1
#
# lower_bound 使用的是半开区间二分模板（同 063）：
#   不断收缩区间，最终 left 落在"第一个 ≥ value"的位置。
#
# 例如：nums = [5,7,7,8,8,10], target = 8
#   left = lower_bound(8)    → 第一个 ≥ 8 的位置 = 3 ✓（8 的位置）
#   right = lower_bound(9) - 1 → 第一个 ≥ 9 的位置 = 5 - 1 = 4 ✓（最后一个 8）
#   返回 [3, 4]
#
#   nums = [5,7,7,8,8,10], target = 6
#   left = lower_bound(6) → 第一个 ≥ 6 的位置 = 1
#   nums[1] = 7 ≠ 6 → 未找到 → 返回 [-1, -1]
#
# 时间复杂度：O(log n)——两次二分
# 空间复杂度：O(1)

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]   # [target 的起始位置, 结束位置]，未找到则 [-1, -1]
        """

        def lower_bound(value):
            """查找第一个 ≥ value 的位置（即二分插入位置）。
            使用半开区间 [left, right)。
            """
            left = 0
            right = len(nums)

            while left < right:
                mid = (left + right) // 2

                if nums[mid] < value:
                    left = mid + 1    # 中间值太小 → 答案在右边
                else:
                    right = mid       # 中间值 ≥ value → mid 可能就是答案

            return left  # left == right，即第一个 ≥ value 的位置

        left_position = lower_bound(target)

        # 注意顺序：先判越界，再取值比较！
        # 否则 target 大于所有元素时 left_position == len(nums) 会越界
        if left_position == len(nums) or nums[left_position] != target:
            return [-1, -1]

        # 右边界 = 第一个 > target 的位置 - 1
        right_position = lower_bound(target + 1) - 1

        return [left_position, right_position]
