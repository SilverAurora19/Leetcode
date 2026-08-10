# LeetCode 22: 括号生成 (Generate Parentheses)
#
# 题目：给定 n，生成所有由 n 对括号组成的有效括号组合。
# 有效：任何时候右括号不能多于左括号，最终左右各 n 个。
#
# 核心思路（回溯 + 条件剪枝）：
# 这道题的"选择列表"由两个条件动态决定，而不是遍历一个固定的集合：
#   - 可以放 '('：只要还没放够 n 个左括号（left < n）
#   - 可以放 ')'：只要右括号数 < 左括号数（right < left）
#
# 第二个条件是保证括号有效性的关键——
# 如果 right >= left 还放 ')'，就会出现像 ")" 或 "())" 这样的无效前缀。
#
# 决策树（n = 2）：
#                              []
#                              |
#                             '('              ← 只能放 '('（不能以 ')' 开头）
#                          /         \
#                      '(('          '()'      ← left < n 可继续 '('，right < left 可放 ')'
#                     /                \
#                  '(()'              '()('
#                   /                   \
#                '(())'              '()()'    ← left==2, right==2 → 收集
#
#   状态用 (left, right, path) 表示：
#   (0,0,"")
#     → (1,0,"(")                                 # left<2 → '('
#       → (2,0,"((")                               # left<2 → '('
#         → (2,1,"(()")                            # left=2 不能 '('; right<left → ')'
#           → (2,2,"(())") → 收集 ✓                # right<left → ')'; 收集
#       → (1,1,"()")                               # right<left → ')'
#         → (2,1,"()(")                            # left<2 → '('
#           → (2,2,"()()") → 收集 ✓                # right<left → ')'; 收集
#
#   结果：["(())", "()()"]，共 2 种（第 2 个卡特兰数 C₂ = 2）
#
# 时间复杂度：O(4^n / √n)——第 n 个卡特兰数，有效括号组合的总数约 4^n/(n√n)
# 空间复杂度：O(n)——递归栈深度 + path 数组

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]   # 所有有效括号组合
        """
        result = []
        path = []   # 当前正在构建的括号字符串

        def backtrack(left, right):
            """
            回溯：left = 已放的 '(' 数，right = 已放的 ')' 数
            """
            # 终止条件：左右括号各放够 n 个 → 收集结果
            if left == n and right == n:
                result.append(''.join(path))
                return

            # 选择1：放 '(' —— 还剩左括号可用
            if left < n:
                path.append('(')
                backtrack(left + 1, right)
                path.pop()   # 回溯，撤销选择

            # 选择2：放 ')' —— 必须保证右括号数 < 左括号数才能放
            #         否则会出现像 ")" 或 "())" 这种无效前缀
            if right < left:
                path.append(')')
                backtrack(left, right + 1)
                path.pop()   # 回溯，撤销选择

        backtrack(0, 0)
        return result
