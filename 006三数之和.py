# 三数之和先排序，固定一个数，剩下两个数用左右指针寻找，并分别处理固定数和左右指针的重复。
class Solution(object):
    def threeSum(self,nums):
        nums.sort()     # sort() 是列表的方法，会修改原列表
        result = []
        n = len(nums)        

        for first in range(n-2):
            if nums[first] > 0:
                break
            if first > 0 and nums[first] == nums[first - 1]:
                continue

            left = first + 1
            right = n - 1

            while left < right:
                total = nums[first] + nums[left] + nums[right]

                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    result.append([nums[first],nums[left],nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return result
