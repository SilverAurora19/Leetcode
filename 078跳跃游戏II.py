# LeetCode 45: 跳跃游戏 II (Jump Game II)
#
# 题目：数组每个元素表示"从该位置最多能跳几步"，求跳到终点的最少跳跃次数。
# （题目保证一定能到达终点）
#
# 核心思路（贪心，按"跳跃范围"分层）：
# 把跳跃过程看成一层层向外扩张（类似 BFS）：
#   - current_end：当前这一跳能覆盖的最远边界
#   - farthest：在当前覆盖范围内，再跳一次能到达的最远位置
#
# 遍历时不断更新 farthest。
# 当走到 current_end 边界时，说明"当前这一跳的范围用完了"，
# 必须再跳一次，于是 jumps+1，并把 current_end 更新为 farthest。
#
# 为什么是"最少"？
#   因为我们每次都把"再跳一次能到的最远"作为新的边界，
#   贪心地让每一跳都覆盖尽可能远，跳数自然最少。
#
# 例如：nums = [2, 3, 1, 1, 4]
#   初始：jumps=0, current_end=0, farthest=0
#   i=0(2)：farthest = max(0, 0+2)=2；i==current_end(0) → jumps=1, current_end=2
#   i=1(3)：farthest = max(2, 1+3)=4；i≠current_end
#   i=2(1)：farthest = max(4, 2+1)=4；i==current_end(2) → jumps=2, current_end=4
#   i=3(1)：farthest = max(4, 3+1)=4；i≠current_end
#   循环到 len-1=3 结束 → 返回 jumps=2
#   （路径：第1跳从0到1，第2跳从1到4）
#
# 注意：循环到 len(nums)-1 为止（不包括最后一个），
#   因为到达终点前最后一个位置时就该结算了，不需要处理终点本身。
#
# 时间复杂度：O(n)
# 空间复杂度：O(1)

class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int   # 到达终点的最少跳跃次数
        """
        jumps = 0         # 已跳的次数
        farthest = 0      # 当前覆盖范围内，再跳一次能到的最远位置
        current_end = 0   # 当前这一跳能覆盖的最远边界

        for i in range(len(nums) - 1):   # 不处理终点本身
            # 更新"从当前覆盖范围内出发，最远能到哪"
            farthest = max(farthest, i + nums[i])

            # 走到了当前跳跃的边界 → 必须再跳一次
            if i == current_end:
                jumps += 1               # 跳数 +1
                current_end = farthest   # 新的边界 = 最远能到的地方

        return jumps
