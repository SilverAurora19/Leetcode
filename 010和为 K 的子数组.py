# 当前前缀和减去 k，就是需要寻找的历史前缀和；它出现过几次，就有几个以当前位置结尾的合法子数组。
class Solution(object):
    def subarraySum(self, nums, k):
        """
        找到数组 nums 中和为 k 的连续子数组的个数。

        思路：前缀和 + 哈希表
        设 prefix_sum 为当前的前缀和（从 nums[0] 到当前元素的累加和）。
        若存在某个之前的前缀和等于 prefix_sum - k，则这两个位置之间的子数组之和就是 k。
        哈希表 prefix_count 记录每个前缀和出现的次数，
        这样就能在 O(1) 时间内查到有多少个前缀和等于 prefix_sum - k。
        """
        # 这个字典保存：某个前缀和 → 这个前缀和之前出现了多少次
        prefix_count = {0: 1}   # 初始化：前缀和为 0 出现 1 次（处理子数组从头开始的情况）
        prefix_sum = 0          # 当前前缀和
        result = 0              # 和为 k 的子数组个数

        for num in nums:
            prefix_sum += num                    # 更新当前前缀和
            needed = prefix_sum - k              # 需要的前缀和：prefix_sum - k

            # 如果之前出现过 needed，则从那些位置到当前位置的子数组之和为 k
            if needed in prefix_count:
                result += prefix_count[needed]   # 累加满足条件的子数组个数

            # 将当前前缀和记入哈希表
            if prefix_sum in prefix_count:
                prefix_count[prefix_sum] += 1
            else:
                prefix_count[prefix_sum] = 1

        return result
    


