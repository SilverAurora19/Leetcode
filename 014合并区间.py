# 核心思路：
# 1. 先按区间起点从小到大排序，保证遍历时区间按时间线排列。
# 2. 依次遍历每个区间，判断是否与"上一个已合并的区间"重叠：
#    - 不重叠（当前起点 > 上一个终点）：直接加入结果列表，另起新区间。
#    - 有重叠：延长上一个区间的终点，取两者终点的较大值。
#
# 时间复杂度：O(n log n)（排序）
# 空间复杂度：O(n)（结果列表）
# 区间先按起点排序；当前起点超过上个终点就新建，否则把上个终点扩展到更远的位置。

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]   # 二维数组，每个子数组 [start, end]
        :rtype: List[List[int]]            # 返回合并后的区间列表
        """
        # 按区间起点从小到大排序，key 取每个区间的第0个元素（start）
        intervals.sort(key=lambda interval: interval[0])

        merged = []  # 存放合并后的结果

        for start, end in intervals:
            # 情况1：结果为空，或当前区间与上一个不重叠 → 直接加入
            if not merged or start > merged[-1][1]:
                merged.append([start, end])
            # 情况2：有重叠 → 延长上一个区间的终点（取较大者）
            else:
                merged[-1][1] = max(merged[-1][1], end)

        return merged
