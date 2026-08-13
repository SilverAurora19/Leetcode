# LeetCode 51: N 皇后 (N-Queens)
#
# 题目：在 n×n 的棋盘上放置 n 个皇后，使它们互不攻击。
# 皇后可以攻击同一行、同一列、同一条对角线上的棋子。
#
# 核心思路（回溯 + 集合剪枝）：
# 题目的约束决定了每行有且仅有一个皇后。
# 所以我们按行递归：在第 r 行尝试每一列，若能放下就继续下一行。
#
# 关键在于快速判断"是否能放"：
#   - 同一列：用集合 `columns` 标记哪些列已被占
#   - 对角线 1（左上→右下）：同一条对角线上的格子满足 r - c 相同
#   - 对角线 2（右上→左下）：同一条对角线上的格子满足 r + c 相同
#
# 对角线编号的直观理解（n=4）：
#   r-c 的值：           r+c 的值：
#   [ 0 -1 -2 -3]        [0  1  2  3]
#   [ 1  0 -1 -2]        [1  2  3  4]
#   [ 2  1  0 -1]        [2  3  4  5]
#   [ 3  2  1  0]        [3  4  5  6]
#   同一斜线 r-c 相同      同一斜线 r+c 相同
#
# 时间复杂度：O(n!)——第一行 n 种选择，第二行约 n-1 种...
# 空间复杂度：O(n)——棋盘 + 三个集合

class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]   # 所有合法摆放方案
        """
        res = []
        board = [['.'] * n for _ in range(n)]  # n×n 棋盘，初始全为 '.'

        columns = set()  # 被占用的列
        dig1 = set()     # 被占用的对角线 1（左上→右下，特征值 r-c）
        dig2 = set()     # 被占用的对角线 2（右上→左下，特征值 r+c）

        def backtrack(r):
            """在第 r 行尝试放置皇后"""
            # 所有行都放完了 → 记录当前棋盘状态
            if r == n:
                solution = []
                for board_row in board:
                    solution.append(''.join(board_row))   # 把字符数组拼成字符串
                res.append(solution)
                return

            # 尝试在当前行的每一列放皇后
            for c in range(n):
                # 剪枝：列、两条对角线任一被占 → 跳过
                if (c in columns
                        or r - c in dig1
                        or r + c in dig2):
                    continue

                # 放置皇后，标记占用
                board[r][c] = 'Q'
                columns.add(c)
                dig1.add(r - c)
                dig2.add(r + c)

                # 递归处理下一行
                backtrack(r + 1)

                # 回溯：撤销放置，尝试下一列
                board[r][c] = '.'
                columns.remove(c)
                dig1.remove(r - c)
                dig2.remove(r + c)

        backtrack(0)
        return res
