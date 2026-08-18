# LeetCode 55: 跳跃游戏 (Jump Game)
#
# 题目：数组每个元素表示"从该位置最多能跳几步"，判断能否从起点跳到终点。
#
# 核心思路（贪心，维护最远可达距离）：
# 只维护一个变量 max_reach = 目前能跳到的最远下标。
# 遍历每个位置 i：
#   - 如果 i > max_reach → 这个位置根本到不了 → 直接失败
#   - 否则，从 i 出发能跳到 i + jump，更新 max_reach
# 如果全程没有"到不了"的位置，最终一定能到终点。
#
# 关键理解：
#   不需要模拟每一步怎么跳，只要知道"最远能到哪"。
#   因为如果能到 i，那么 i 之前的所有位置也都一定能到（一路跳过去），
#   所以只需要不断扩张最远边界即可。
#
# 例如：nums = [2, 3, 1, 1, 4]
#   i=0, jump=2：max_reach = max(0, 0+2) = 2
#   i=1, jump=3：max_reach = max(2, 1+3) = 4  ← 已经能到终点
#   i=2, jump=1：max_reach = max(4, 2+1) = 4
#   i=3, jump=1：max_reach = max(4, 3+1) = 4
#   i=4, jump=4：max_reach = max(4, 4+4) = 8
#   全程没有 i > max_reach → 返回 True ✓
#
# 反例：nums = [3, 2, 1, 0, 4]
#   i=0：max_reach = 3
#   i=1：max_reach = max(3, 3) = 3
#   i=2：max_reach = max(3, 3) = 3
#   i=3：max_reach = max(3, 3) = 3（jump=0，跳不动）
#   i=4：4 > max_reach=3 → 到不了 → 返回 False ✓
#
# 时间复杂度：O(n)
# 空间复杂度：O(1)

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool   # 能否跳到终点
        """
        max_reach = 0   # 当前能到达的最远下标

        for i in range(len(nums)):
            # 当前位置比最远可达还远 → 根本到不了这里
            if i > max_reach:
                return False

            # 从当前位置出发，更新最远可达距离
            max_reach = max(max_reach, i + nums[i])

        return True   # 全程都能到达，最终一定到终点
