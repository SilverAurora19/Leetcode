class Solution(object):
    def subarraySum(self, nums, k):
        prefix_count = {0:1}
        result = 0
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            need = prefix_sum - k

            if need in prefix_count:
                result += prefix_count[need]

            if prefix_sum in prefix_count:
                prefix_count[prefix_sum] += 1
            else:
                prefix_count[prefix_sum]=1

        return result
