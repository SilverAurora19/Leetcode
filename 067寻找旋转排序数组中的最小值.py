# LeetCode 153: 寻找旋转排序数组中的最小值 (Find Minimum in Rotated Sorted Array)
#
# 题目：在一个"被旋转过的"无重复升序数组中找最小值。
# 例如：[3,4,5,1,2] 是在 [1,2,3,4,5] 基础上旋转得到的，最小值是 1。
#
# 核心思路（二分查找，比较 nums[mid] 和 nums[right]）：
# 旋转数组分成两段，每一段各自有序，最小值就是"旋转点"。
# 每次拿 nums[mid] 和 nums[right] 比较，判断最小值在左半还是右半：
#
#   若 nums[mid] > nums[right] → 说明 mid 在左半段（较大的那半），
#       最小值一定在 mid 右边 → left = mid + 1
#
#   若 nums[mid] < nums[right] → 说明 mid 在右半段（较小的那半），
#       最小值可能是 mid 或更左边 → right = mid（不能 mid-1，mid 可能就是最小值）
#
# 关键：为什么和 right 比较，而不是和 left 比较？
#   因为 nums[mid] > nums[right] 是"旋转点"的确定信号，
#   而 nums[mid] 和 nums[left] 的关系在旋转后不唯一。
#
# 例如：nums = [3, 4, 5, 1, 2]
#   mid=2 → nums[2]=5 > nums[4]=2 → 最小值在右边 → left=3
#   mid=3 → nums[3]=1 < nums[4]=2 → 最小值可能在 mid 或左边 → right=3
#   left==right==3 → 返回 nums[3] = 1 ✓
#
# 时间复杂度：O(log n)
# 空间复杂度：O(1)

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]   # 旋转后的升序数组（无重复元素）
        :rtype: int             # 数组中的最小值
        """
        left = 0
        right = len(nums) - 1

        # 闭区间 [left, right]，当 left == right 时只剩一个候选，就是最小值
        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # mid 落在较大的左半段 → 最小值一定在右边
                left = mid + 1
            else:
                # nums[mid] < nums[right] → mid 落在较小的右半段
                # mid 本身可能就是最小值，所以 right = mid 而不是 mid - 1
                right = mid

        # 收敛到 left == right，就是最小值的位置
        return nums[left]
