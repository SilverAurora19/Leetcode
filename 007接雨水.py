# 核心思路（双指针 + 两边最大高度）：
# 每个位置能接的雨水 = min(左边最高墙, 右边最高墙) - 当前柱高。
#
# 双指针 left/right 从两端向中间收敛：
# - max_left：当前左侧遇到的最高柱子
# - max_right：当前右侧遇到的最高柱子
# - 哪侧的"最大高度"更小，就处理那侧，因为水位由较矮的一侧决定。
#
# 时间复杂度：O(n)
# 空间复杂度：O(1)

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]   # 柱子高度数组
        :rtype: int               # 可接的雨水总量
        """
        left = 0
        right = len(height) - 1

        total_water = 0
        max_left = 0   # 当前已扫描的左侧最高柱子
        max_right = 0  # 当前已扫描的右侧最高柱子

        while left < right:
            # 实时更新左右两侧的最高柱子
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])

            # 哪侧最高柱子更小，水位由该侧决定，处理该侧
            if max_left < max_right:
                # 左最高墙更低 → 当前位置水位 = max_left - 当前柱高
                total_water += max_left - height[left]
                left += 1
            else:
                # 右最高墙更低或相等 → 当前位置水位 = max_right - 当前柱高
                total_water += max_right - height[right]
                right -= 1

        return total_water
