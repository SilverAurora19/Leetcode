class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int   # 和为 k 的连续子数组个数
        """
        prefix_count = {0: 1}  # 前缀和为 0 出现 1 次，处理子数组从头开始的情况
        result = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num          # 更新前缀和
            need = prefix_sum - k      # 需要寻找的历史前缀和

            # 如果之前出现过 need，则从那些位置到当前位置的子数组和为 k
            if need in prefix_count:
                result += prefix_count[need]

            # 将当前前缀和记录到哈希表
            if prefix_sum in prefix_count:
                prefix_count[prefix_sum] += 1
            else:
                prefix_count[prefix_sum] = 1

        return result
