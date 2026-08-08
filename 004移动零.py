# 核心思路（双指针）：
# - right 指针从左到右遍历每个元素，负责"发现"非零元素。
# - left 指针指向"下一个非零元素应该放的位置"。
#
# 当 right 发现非零元素时，与 left 处元素交换，left 右移一位。
# 所有非零元素按原顺序移到前面，零自然被挤到末尾。
#
# 时间复杂度：O(n)
# 空间复杂度：O(1)

class Solution(object):
    def moveZero(self, nums):
        """
        :type nums: List[int]
        :rtype: None   # 原地修改，不返回
        """
        left = 0  # 下一个非零元素应该放置的位置

        for right in range(len(nums)):
            if nums[right] != 0:
                # 两个位置不同时才交换，避免无意义的自我交换
                if nums[right] != nums[left]:
                    nums[left], nums[right] = nums[right], nums[left]

                left += 1  # left 前移，为下一个非零元素预留位置
