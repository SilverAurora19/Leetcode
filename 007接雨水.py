# 每个位置的水量等于左右最高墙的较小值减去当前柱高；双指针每次处理最高边界较小的一侧。
class Solution(object):
    def trap(self,height):
        left = 0
        right = len(height) - 1

        total_water = 0
        max_left = 0
        max_right = 0

        while left < right:
            max_left = max(max_left,height[left])
            max_right = max(max_right,height[right])

            if max_left < max_right:
                total_water += max_left - height[left]
                left += 1
            else:
                total_water += max_right -height[right]
                right -= 1
            
        return total_water