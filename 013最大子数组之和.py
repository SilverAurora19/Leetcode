# 核心思路（Kadane算法）：
# 遍历到当前数字时，只需要判断：
#   是让当前数字单独开始一个新子数组，
#   还是把它接在前面的子数组后面。
# 两者取较大值作为"以当前位置结尾的最大子数组和"。
# 以当前数字结尾时，要么接着前面的最优子数组，要么从当前数字重新开始，选择和更大的方案。

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]    # 整数数组
        :rtype: int              # 返回最大子数组之和
        """
        # 初始化：当前子数组和、全局最大和 都设为第一个元素
        current_sum = nums[0]  # 以当前位置结尾的最大子数组和
        max_sum = nums[0]      # 全局最大子数组和

        # 从第二个元素开始遍历
        for num in nums[1:]:    # 从下标 1 开始，一直到列表末尾
            # 决策：要么另起炉灶（num本身），要么继续累加（current_sum + num）
            current_sum = max(num, current_sum + num)
            # 更新全局最大值
            max_sum = max(max_sum, current_sum)

        return max_sum
