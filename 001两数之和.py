# 核心目标：遍历到当前数字 num 时，快速判断之前是否出现过 target - num。
# 遍历当前数字时，先在字典中寻找补数；找不到，再把当前数字和下标存进去。
class Solution(object):
    def twoSum(self,nums,target):
        seen={}

        for i,num in enumerate(nums):
            need = target - num
            
            if need in seen:
                return [seen[need],i]
            
            seen[num] = i

"""
字典保存映射关系
num_to_index[num] = index
"""