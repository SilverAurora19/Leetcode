# LeetCode 17: 电话号码的字母组合 (Letter Combinations of a Phone Number)
#
# 题目：给定一个数字字符串 digits（2-9），返回它所有可能的字母组合。
# 每个数字对应一组字母（老式手机键盘映射），从每个数字的字母中各选一个。
#
# 核心思路（回溯 / 多组各选一个）：
# 和全排列、子集不同，这道题是"每个位置有自己独立的选择池"：
#   - 全排列：从一个池里选，不能重复 → used 数组
#   - 子集：  从一个池里选，不能回头 → start_index
#   - 本题：  每个位置独立，从自己的池里各选一个 → 用 index 标识当前处理到第几个数字
#
# 决策树是"定长"的——每个组合的长度 = digits 的长度。
# 每个数字是一层，该数字对应的字母是这一层的分支选项。
#
# 例如：digits = "23"
#
#   键盘映射：'2' → "abc", '3' → "def"
#
#   决策树（第0层index=0处理'2'，第1层index=1处理'3'）：
#                   ""
#           /       |       \           ← index=0: 从 '2' 的 {a,b,c} 中选
#          a        b        c
#        / | \    / | \    / | \         ← index=1: 从 '3' 的 {d,e,f} 中选
#       ad ae af bd be bf cd ce cf       ← index==2==len → 收集结果
#
#   共 3×3 = 9 种组合
#
# 对比前面的回溯题：
#   056 子集：   用 start_index 保证不回头 → 每个元素"选或不选"
#   055 全排列： 用 used 数组标记用过没有 → 每次从剩余中选
#   057 本题：   用 index 标识当前处理到第几个位置 → 每个位置从独立的池中选
#
# 时间复杂度：O(4^n)——最坏情况每个数字对应 4 个字母（如 '7'→pqrs, '9'→wxyz）
#              共有最多 4^n 种组合，每种组合 O(n) 用于 join
# 空间复杂度：O(n)——递归栈深度 = digits 长度，path 数组也是 n

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]   # 所有字母组合
        """
        # 空输入 → 空结果（注意：不是 [""]）
        if not digits:
            return []

        # 电话键盘映射：数字 → 可选字母
        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        path = []     # 当前组合（存字符列表，最后 join 成字符串）
        result = []   # 所有组合结果

        def backtrack(index):
            """
            回溯：处理 digits[index] 这个数字，从它对应的字母中选一个。
            index：当前处理到 digits 的第几个位置。
            """
            # 终止条件：所有数字都处理完了 → 收集当前组合
            if index == len(digits):
                result.append(''.join(path))
                return

            # 当前数字及其对应的字母池
            digit = digits[index]
            letters = phone[digit]

            # 从当前数字的字母池中，各选一个字母
            for letter in letters:
                # 做选择
                path.append(letter)
                # 递归：处理下一个数字（index + 1）
                backtrack(index + 1)
                # 撤销选择（回溯）
                path.pop()

        backtrack(0)
        return result
