# LeetCode 41: 缺失的第一个正数 (First Missing Positive)
#
# 核心思路（原地哈希 / 循环排序）：
# 题目要求 O(n) 时间 + O(1) 空间，不能排序也不能用哈希表。
#
# 关键洞察：对于长度为 n 的数组，缺失的第一个正数一定在 [1, n+1] 之间。
# 因此我们只需要关注 1~n 范围内的数，忽略 ≤0 和 >n 的数。
#
# 做法：把每个在 [1, n] 范围内的数字 x 放到下标 x-1 的位置上（即"原地哈希"）。
#       放置完毕后再次遍历，第一个不满足 nums[i] == i+1 的位置就是答案；
#       如果全部符合，说明 1~n 全有，答案就是 n+1。
#
# 例如：nums = [3, 4, -1, 1]
#   交换过程：3 放到 idx=2 → [-1, 4, 3, 1]
#            -1 跳过
#            4 放到 idx=3 → [-1, 1, 3, 4]
#            1 放到 idx=0 → [1, -1, 3, 4]
#   最终检查：idx=1 处 -1 ≠ 2，返回 2。
#
# 时间复杂度：O(n)——每个数最多被交换一次
# 空间复杂度：O(1)

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int   # 缺失的第一个正数
        """
        n = len(nums)

        # 第1步：原地哈希——把每个正数放到"它该在的位置"
        for index in range(n):
            # 用 while 而非 if，因为交换过来的新数也可能需要继续放到正确位置
            # 条件说明：
            #   1 <= nums[index] <= n   → 当前数在有效范围内
            #   nums[目标位置] != 当前数  → 目标位置上还没有正确的数（避免死循环）
            while 1 <= nums[index] <= n and nums[nums[index] - 1] != nums[index]:
                target_index = nums[index] - 1      # nums[index] 应该在的下标
                # 交换当前下标和它应该在的下标
                nums[target_index], nums[index] = nums[index], nums[target_index]

        # 第2步：找出第一个"对不上"的位置
        for index in range(n):
            if nums[index] != index + 1:   # 下标 i 应该放 i+1
                return index + 1           # 缺失的最小正数

        # 1~n 全部出现，缺失的是 n+1
        return n + 1
