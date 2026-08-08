# 核心思路（双指针从两端向中间收敛）：
# 面积 = 宽度 × min(左高, 右高)，宽度 = right - left。
# 移动指针时宽度一定变小，因此只能移动较短的那根柱子，才有可能找到更高的边来弥补宽度的损失。
# 如果移动高的那根，面积只会更小（宽度变小了，高度也不可能超过已经更短的短边）。
#
# 时间复杂度：O(n)
# 空间复杂度：O(1)

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]   # 每根柱子的高度
        :rtype: int               # 最大盛水量
        """
        left = 0                        # 左指针
        right = len(height) - 1         # 右指针
        maxArea = 0                     # 记录全局最大面积

        while left < right:
            current_width = right - left
            current_height = min(height[left], height[right])   # 面积由短边决定
            current_area = current_height * current_width

            maxArea = max(maxArea, current_area)

            # 移动较短的那根柱子——宽度一定变小，只能赌高度变大
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea