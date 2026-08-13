# LeetCode 4: 寻找两个正序数组的中位数 (Median of Two Sorted Arrays)
# 这是 Hard 难度，核心是"二分划分"思想。
#
# 核心思路（在较短的数组上二分找分割点）：
# 中位数把合并后的数组分成"左半部分"和"右半部分"，两边元素个数相等（或差 1）。
# 我们在 nums1 上找一个分割点 i，把 nums1 分成左右两半；
# 对应地在 nums2 上分割点 j，使得左半部分总数 = 右半部分总数。
#
#   nums1:  [ ... | ... ]     i 是分割点，左边 i 个元素
#   nums2:  [ ... | ... ]     j 是分割点，左边 j 个元素
#   合并后：左半 = nums1 左边 + nums2 左边，共有 (m+n+1)//2 个元素
#
# 合法分割的条件（左半所有元素 ≤ 右半所有元素）：
#   left1 <= right2 且 left2 <= right1
#   其中 left1 = nums1 左边最大, right1 = nums1 右边最小（类似 left2/right2）
#
# 找到合法分割后：
#   总长度奇数 → 中位数 = 左半的最大值 max(left1, left2)
#   总长度偶数 → 中位数 = (左半最大 + 右半最小) / 2
#
# 为什么只在较短的数组上二分？
#   保证 j = (m+n+1)//2 - i 始终 ≥ 0，减少边界判断。
#
# 为什么要加 ±inf（无穷大/无穷小）？
#   当分割点落在数组边界时（i==0 或 i==m），左边或右边为空，
#   用 -inf 表示"空的那半边没有值，取极值不影响比较"。
#
# 例如：nums1=[1,3], nums2=[2], 合并后 [1,2,3]，中位数 = 2
#   i=1（nums1 左边 [1]，右边 [3]）
#   j=(3+1)//2 - 1 = 1（nums2 左边 [2]，右边 []）
#   left1=1 <= right2=inf ✓，left2=2 <= right1=3 ✓ → 合法
#   总长 3 是奇数 → 中位数 = max(1,2) = 2 ✓
#
# 时间复杂度：O(log(min(m, n)))
# 空间复杂度：O(1)

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 保证 nums1 是较短的数组，减少二分范围
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m          # 在 nums1 上二分搜索分割点 i，范围 [0, m]

        while low <= high:
            i = (low + high) // 2             # nums1 的分割点
            j = (m + n + 1) // 2 - i       # nums2 的分割点（保证左半总数固定）

            # 四个边界值（用 ±inf 处理"某半边为空"的情况）
            left1 = nums1[i - 1] if i > 0 else float('-inf')    # nums1 左半最大
            right1 = nums1[i] if i < m else float('inf')        # nums1 右半最小
            left2 = nums2[j - 1] if j > 0 else float('-inf')    # nums2 左半最大
            right2 = nums2[j] if j < n else float('inf')        # nums2 右半最小

            # 分割合法：左半所有元素 ≤ 右半所有元素
            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 1:
                    # 总长度奇数 → 中位数 = 左半最大值
                    return max(left1, left2)
                else:
                    # 总长度偶数 → 中位数 = (左半最大 + 右半最小) / 2
                    return (max(left1, left2) + min(right1, right2)) / 2.0
            elif left1 > right2:
                # nums1 左半太大 → 分割点 i 需要左移（减小 left1）
                high = i - 1
            else:
                # left2 > right1 → nums1 左半太小 → 分割点 i 需要右移
                low = i + 1
