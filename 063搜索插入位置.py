# LeetCode 35: 搜索插入位置 (Search Insert Position)
#
# 题目：给定有序数组和 target，若 target 存在返回下标，否则返回它应插入的位置。
#
# 核心思路（二分查找，左闭右开半开区间）：
# 使用 `while left < right` 的二分模板，搜索区间 [left, right)。
#   - 中间值 < target → target 在右边，收缩左边界 left = mid + 1
#   - 中间值 >= target → target 可能在中间或左边，收缩右边界 right = mid
# 循环结束后 left == right，这个位置就是答案：
#   要么 target 恰好在这里（找到了），要么是它应该插入的位置（第一个 ≥ target 的位置）。
#
# 为什么用半开区间 [left, right)？
#   当 nums[mid] >= target 时，mid 本身可能就是答案，所以 right = mid 而不是 mid - 1，
#   这恰好保证了最终 left 停在"第一个 ≥ target"的位置。
#
# 例如：nums=[1,3,5,6], target=2
#   mid=1, nums[1]=3 ≥ 2 → right=1
#   mid=0, nums[0]=1 < 2 → left=1
#   left==right==1 → 返回 1（2 应该插在 1 和 3 之间）
#
# 时间复杂度：O(log n)
# 空间复杂度：O(1)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        :type nums: List[int]   # 升序排列的整数数组
        :type target: int
        :rtype: int             # target 的下标或应插入位置
        """
        left = 0
        right = len(nums)         # 半开区间 [left, right)，right 初始 = n

        # 当 left == right 时区间为空，退出
        while left < right:
            mid = (left + right) // 2   # 每次迭代都重新算 mid

            if nums[mid] < target:
                # 中间值太小 → target 一定在右半区（不含 mid）
                left = mid + 1
            else:
                # 中间值 ≥ target → target 可能在 mid 或左半区（保留 mid）
                right = mid

        # 退出时 left == right，就是第一个 ≥ target 的位置
        return left
