# 核心思路（三次反转法）：
# 假设 k = 2，数组 [1,2,3,4,5] → 期望结果 [4,5,1,2,3]
#
# 第1步：反转整个数组 → [5,4,3,2,1]
# 第2步：反转前 k 个     → [4,5,3,2,1]
# 第3步：反转后 n-k 个   → [4,5,1,2,3]
#
# 时间复杂度：O(n)，每个元素被访问常数次
# 空间复杂度：O(1)，原地操作，无额外空间
# 右轮转 k 位：先整体翻转，再翻转前 k 个，最后翻转剩余部分。
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]   # 待旋转的数组
        :type k: int            # 向右旋转的步数
        :rtype: None            # 原地修改，不返回
        """
        n = len(nums)

        # k 可能超过数组长度，取模避免多余的反转（轮转 n 次等于没变）
        k %= n

        # 三次反转
        self.reverse(nums, 0, n - 1)      # 1. 整体反转
        self.reverse(nums, 0, k - 1)      # 2. 反转前 k 个元素
        self.reverse(nums, k, n - 1)      # 3. 反转剩余 n-k 个元素

    def reverse(self, nums, left, right):
        """反转 nums[left..right] 区间内的元素，双指针相向而行"""
        while left < right:
            # 交换左右指针指向的元素
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
