from collections import deque
from typing import List

# 单调队列只保留仍可能成为最大值的下标：过期元素从队头删，比新元素小的候选从队尾删，队头永远是窗口最大值。
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        返回滑动窗口每次移动后窗口内的最大值。

        思路：单调递减队列（存储下标）
        维护一个双端队列 index_queue，其中存储的下标对应的 nums 值是严格递减的，
        因此队头始终是当前窗口的最大值。
        每次窗口滑动时：
        1. 移除队头已经滑出窗口的下标
        2. 移除队尾所有 ≤ 当前新元素的下标（它们不可能再成为最大值）
        3. 将当前元素下标加入队尾
        4. 窗口成型后，队头即为当前窗口最大值
        """
        index_queue = deque()   # 单调递减队列，存放下标（非数值）
        result = []             # 存储每个窗口的最大值

        for right in range(len(nums)):
            left = right - k + 1  # 当前窗口的左边界下标

            # 如果队头下标已经滑出窗口左边界，过期了，踢出去
            if index_queue and index_queue[0] < left:
                index_queue.popleft()

            # 从队尾弹出所有 ≤ 当前新元素的下标，
            # 从而保持队列的单调递减性
            while (
                index_queue
                and nums[index_queue[-1]] <= nums[right]
            ):
                index_queue.pop()

            # 将当前元素下标加入队尾
            index_queue.append(right)

            # 当窗口长度首次达到 k（即 right >= k - 1）后，
            # 队头下标对应的值就是当前窗口的最大值
            if right >= k - 1:
                result.append(nums[index_queue[0]])

        return result