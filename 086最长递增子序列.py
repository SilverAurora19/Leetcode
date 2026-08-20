# LeetCode 300: 最长递增子序列 (Longest Increasing Subsequence)
#
# 题目：求数组中"严格递增"的最长子序列的长度（子序列不必连续）。
#
# 核心思路（二分 + 耐心排序 / Patience Sorting）：
# 维护一个数组 tails，其中 tails[i] = 长度为 i+1 的递增子序列的"最小结尾值"。
# tails 本身是严格递增的，所以可以用二分查找。
#
# 对每个数 num：
#   1. 用二分找 num 在 tails 中应该插入的位置 pos
#   2. 如果 pos == len(tails) → num 比所有结尾都大，可以接在后面，序列变长 → 追加
#   3. 否则 → 用 num 替换 tails[pos]（更小的结尾值，为后续更长的序列留空间）
#
# 为什么替换不会破坏正确性？
#   tails 维护的是"每个长度下的最小结尾"，替换成更小的值
#   只会让未来的序列更容易延长，长度信息依然保留。
#
# 例如：nums = [10, 9, 2, 5, 3, 7, 101, 18]
#   num=10：tails=[10]
#   num=9：9 比 10 小 → 替换 tails[0]=9，tails=[9]
#   num=2：2 比 9 小 → tails=[2]
#   num=5：5 > 2 → 追加，tails=[2,5]
#   num=3：3 替换 5 → tails=[2,3]
#   num=7：7 > 3 → 追加，tails=[2,3,7]
#   num=101：追加，tails=[2,3,7,101]
#   num=18：18 替换 101 → tails=[2,3,7,18]
#   最终长度 = 4（对应 [2,3,7,18] 或 [2,5,7,101] 等）
#
# 注意：tails 数组不一定等于真实的 LIS，只是长度正确。
#
# 时间复杂度：O(n log n)——每个数一次二分
# 空间复杂度：O(n)——tails 数组

from typing import List
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int   # 最长递增子序列的长度
        """
        tails = []   # tails[i] = 长度为 i+1 的递增子序列的最小结尾值

        for num in nums:
            # 二分查找 num 应插入的位置（第一个 ≥ num 的位置）
            pos = bisect_left(tails, num)

            if pos == len(tails):
                # num 比所有结尾都大 → 可以延长序列
                tails.append(num)
            else:
                # 用更小的 num 替换，为将来更长的序列留余地
                tails[pos] = num

        return len(tails)
