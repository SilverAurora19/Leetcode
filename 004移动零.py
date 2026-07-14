"""
双指针交换

- `right` 从左到右检查每个元素。
- `left` 表示下一个非零元素应该放在哪里。

当 `nums[right]` 是非零元素时：
1. 把它和 `nums[left]` 交换。
2. 让 `left` 向右移动一位。
"""
class Solution(object):
    def moveZero(self,nums):
        left = 0
        
        for right in range(len(nums)):
            if nums[right] != 0:
                if nums[right] != nums[left]:   # 判断两个位置是否相同。可以避免没有意义的交换操作。
                    nums[left],nums[right] = nums[right],nums[left]
                
                left += 1