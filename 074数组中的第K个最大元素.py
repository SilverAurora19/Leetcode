# LeetCode 215: 数组中的第 K 个最大元素 (Kth Largest Element in an Array)
#
# 题目：在未排序的数组中找第 k 大的元素（注意是"最大"，不是"最小"）。
#
# 核心思路（快速选择 QuickSelect）：
# 快速排序的"分治"变体——每轮只处理包含答案的那一半，不用完全排序。
#
# 步骤：
#   1. 随机选一个基准值 pivot（随机化避免最坏情况 O(n²)）
#   2. 把数组分成三份：
#      - left：所有 > pivot 的元素（比基准大）
#      - mid：所有 == pivot 的元素
#      - right：所有 < pivot 的元素
#   3. 判断第 k 大落在哪一份：
#      - k ≤ len(left)          → 答案在 left 里，递归找 left
#      - k ≤ len(left)+len(mid) → 答案就是 pivot（落在 mid 里）
#      - 否则                    → 答案在 right 里，递归找 right（k 要减去前面那些）
#
# 例如：nums = [3,2,1,5,6,4], k=2（找第2大 = 5）
#   pivot 假设 = 3
#   left = [5,6,4]（>3）, mid = [3], right = [2,1]（<3）
#   k=2 ≤ len(left)=3 → 递归 left=[5,6,4], k=2
#     pivot 假设 = 4
#     left = [5,6], mid=[4], right=[]
#     k=2 ≤ len(left)=2 → 递归 left=[5,6], k=2
#       pivot 假设 = 6
#       left=[], mid=[6], right=[5]
#       k=2 ≤ len(mid)=1 → 返回 6？不对，这里 k=2 > len(left)=0
#       且 k=2 > len(left)+len(mid)=1 → 递归 right=[5], k=2-1=1
#       left=[], mid=[5], k=1 ≤ len(mid)=1 → 返回 5 ✓
#
# 平均时间复杂度：O(n)（每轮减半，n + n/2 + n/4 + ... = 2n）
# 最坏时间复杂度：O(n²)（但随机化 pivot 让概率极低）
# 空间复杂度：O(n)（每轮创建三个新列表）

import random  # 修：补充 import random

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int   # 第 k 大的元素
        """
        # 随机选基准值，避免"每次选到最小/最大"导致退化成 O(n²)
        pivot = random.choice(nums)

        # 按与 pivot 的大小关系分成三份
        left = [x for x in nums if x > pivot]    # 比基准大的
        mid = [x for x in nums if x == pivot]    # 等于基准的
        right = [x for x in nums if x < pivot]   # 比基准小的

        # 判断答案落在哪一份
        if k <= len(left):
            # 第 k 大在"更大的那一半"里
            return self.findKthLargest(left, k)
        elif k <= len(left) + len(mid):
            # 第 k 大正好是 pivot（落在 mid 这一堆里）
            return pivot
        else:
            # 第 k 大在"更小的那一半"里，k 要减去已经排除的元素个数
            return self.findKthLargest(right, k - len(left) - len(mid))
