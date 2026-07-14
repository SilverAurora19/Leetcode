# 最重要的思路是：只有当 num - 1 不在集合中时，num 才可能是一段连续序列的起点。
# 只有前一个数字不存在时，当前数字才是连续序列的起点；只从起点向后查找，才能避免重复计算。
class Solution(object):
    def longestConsecutive(self, nums):
        nums_set = set(nums)
        max_lens = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                current = num
                current_lens = 1

                while current + 1 in nums_set:
                    current += 1
                    current_lens += 1

                max_lens = max(current_lens,max_lens)

        return max_lens

