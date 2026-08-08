# 核心思路（哈希表）：
# 遍历到当前数字 num 时，快速判断之前是否出现过 target - num。
# 用字典保存"值 → 下标"，每次先查补数，找不到就把当前数字和下标存进去。
# 这样一趟遍历即可找到答案。
#
# 时间复杂度：O(n)
# 空间复杂度：O(n)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]   # 返回两个数的下标，和为 target
        """
        seen = {}  # 字典：值 → 下标，存储已经遍历过的数字

        for i, num in enumerate(nums):
            need = target - num  # 需要配对的值

            # 在当前数字之前查找补数
            if need in seen:
                return [seen[need], i]  # 返回 [补数下标, 当前数下标]

            # 没找到，把当前数字存入字典
            seen[num] = i
