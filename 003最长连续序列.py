# 核心思路（哈希集合 + 只从起点开始数）：
# 要求 O(n) 时间，意味着不能排序。
# 关键洞察：只有当 num - 1 不在集合中时，num 才是一段连续序列的起点。
# 只从起点向后查找，每个元素最多被访问两次，避免了 O(n²) 的重复计算。
#
# 时间复杂度：O(n)
# 空间复杂度：O(n)

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int   # 最长连续序列的长度
        """
        nums_set = set(nums)  # 转成集合，O(1) 判断某个数字是否存在
        max_lens = 0           # 全局最长连续序列长度

        for num in nums_set:
            # 只有当 num-1 不在集合中时，num 才是连续序列的起点
            # 这样可以保证每个连续序列只被统计一次
            if num - 1 not in nums_set:
                current = num
                current_lens = 1

                # 从起点向后数，看能连续到多远
                while current + 1 in nums_set:
                    current += 1
                    current_lens += 1

                max_lens = max(current_lens, max_lens)

        return max_lens
