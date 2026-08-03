# LeetCode 239: 滑动窗口最大值 (Sliding Window Maximum)
#
# 核心思路（单调递减队列）：
# 维护一个双端队列，队列中存的是下标，对应 nums 值严格递减。
# 这样队头永远是当前窗口的最大值。
#
# 关键操作（每个新元素到来时）：
#   1. 踢过期：队头下标如果已经滑出窗口左边界 → 从左边弹出
#   2. 踢弱者：队尾所有 ≤ 新元素的值 → 从右边弹出（它们永远没机会当最大值了）
#   3. 入队：把新元素下标从右边加入
#   4. 收答案：窗口成型后（right >= k-1），队头就是当前窗口最大值
#
# 为什么可以放心踢掉"弱者"？
#   因为它们在新元素之前且更小，后面的窗口中只要它们还在，新元素也一定在，
#   而新元素比它们大，它们永远翻不了身。
#
# 例如：nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
#
#   right=0, num=1：队空 → 入队[1]                   窗口未成型
#   right=1, num=3：队尾1≤3，弹出1 → 入队[3]          窗口未成型
#   right=2, num=-1：队尾3> -1 → 入队[3,-1]          窗口成型 → 队头nums[3]=3
#   right=3, num=-3：队尾-1> -3 → 入队[3,-1,-3]      窗口成型 → 队头nums[3]=3
#   right=4, num=5 ：过期检查通过，队尾-3≤5弹出，队尾-1≤5弹出，队尾3≤5弹出 → 入队[5] → 队头nums[5]=5
#   right=5, num=3 ：队尾5>3 → 入队[5,3]             窗口成型 → 队头nums[5]=5
#   right=6, num=6 ：队尾3≤6弹出，队尾5≤6弹出 → 入队[6] 窗口成型 → 队头nums[6]=6
#   right=7, num=7 ：队尾6≤7弹出 → 入队[7]            窗口成型 → 队头nums[7]=7
#
#   结果：[3, 3, 5, 5, 6, 7]
#
# 时间复杂度：O(n)——每个元素入队一次、出队一次
# 空间复杂度：O(k)——队列最多存 k 个元素

from collections import deque
from typing import List


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int            # 窗口大小
        :rtype: List[int]       # 每个窗口的最大值
        """
        index_queue = deque()   # 单调递减队列，存的是下标（不是值）
        result = []

        for right in range(len(nums)):
            left = right - k + 1  # 当前窗口的左边界下标

            # 1. 踢过期：队头下标 < 左边界 → 已滑出窗口
            if index_queue and index_queue[0] < left:
                index_queue.popleft()

            # 2. 踢弱者：队尾对应值 ≤ 新元素 → 它们永远没机会当最大值
            while (
                index_queue
                and nums[index_queue[-1]] <= nums[right]
            ):
                index_queue.pop()

            # 3. 入队：把当前元素下标从右边加入
            index_queue.append(right)

            # 4. 收答案：窗口一成型（right >= k-1），队头就是最大值
            if right >= k - 1:
                result.append(nums[index_queue[0]])

        return result
