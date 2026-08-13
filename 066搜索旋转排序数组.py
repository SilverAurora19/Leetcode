# LeetCode 33: 搜索旋转排序数组 (Search in Rotated Sorted Array)
#
# 题目：在一个"被旋转过的"有序数组中搜索 target。
# 例如：[4,5,6,7,0,1,2] 是在 [0,1,2,4,5,6,7] 的基础上从"4"处旋转得到的。
# 要求 O(log n)。
#
# 核心思路（二分查找 + 判断有序半区）：
# 旋转数组的特点是："左半段"和"右半段"各自有序。
# 拿 nums[mid] 和 nums[left] 比较，可以判断 mid 落在哪个半区：
#
#   若 nums[left] <= nums[mid] → 左半区 [left, mid] 是有序的
#     - 如果 target 正好在这个有序区间内 → 去左边找
#     - 否则 → 去右边找
#
#   若 nums[left] > nums[mid] → 右半区 [mid, right] 是有序的（旋转点在左边）
#     - 如果 target 正好在这个有序区间内 → 去右边找
#     - 否则 → 去左边找
#
# 例如：nums = [4,5,6,7,0,1,2], target = 0
#   mid=3 → nums[3]=7, 左半区 [4,5,6,7] 有序
#   0 不在 [4,7] → 去右边 [0,1,2]
#   mid=5 → nums[5]=1, 左半区 [0,1] 有序
#   0 在 [0,1] 中 → 去左边 → 最终找到 0
#
# 时间复杂度：O(log n)
# 空间复杂度：O(1)

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]   # 旋转后的升序数组（无重复元素）
        :type target: int
        :rtype: int             # target 的下标，不存在返回 -1
        """
        left = 0
        right = len(nums) - 1

        # 闭区间 [left, right]，所以用 <= 而不是 <
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # 判断哪半边是有序的
            if nums[left] <= nums[mid]:
                # 左半区 [left, mid] 有序
                if nums[left] <= target < nums[mid]:
                    # target 在左半区 → 缩小到左边
                    right = mid - 1
                else:
                    # target 不在左半区 → 去右边找
                    left = mid + 1
            else:
                # 右半区 [mid, right] 有序
                if nums[mid] < target <= nums[right]:
                    # target 在右半区 → 缩小到右边
                    left = mid + 1
                else:
                    # target 不在右半区 → 去左边找
                    right = mid - 1

        return -1
