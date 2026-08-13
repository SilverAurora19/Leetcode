# LeetCode 79: 单词搜索 (Word Search)
#
# 题目：在 m×n 的字母矩阵中，找一条相邻路径使得连起来的字母等于给定单词。
# 每个格子只能走一次，上下左右四个方向。
#
# 核心思路（DFS 回溯）：
# 遍历矩阵每个格子作为起点，向四个方向深度优先搜索。
#   1. 当前格字符匹配 → 标记为已访问（用特殊字符占位，避免额外空间）
#   2. 向上下左右四个方向递归搜索下一个字符
#   3. 四个方向搜完都没找到 → 回溯，恢复当前格的原始字符
#
# 回溯的关键：搜完一条路径后要"撤销选择"，让兄弟路径能正常使用这个格子。
#
# 例如：board = [["A","B","C","E"],
#                ["S","F","C","S"],
#                ["A","D","E","E"]]
#       word = "ABCCED"
#
#   从 (0,0)='A' 开始：
#     A(0,0) → B(0,1) → C(0,2) → C(1,2) → E(1,3)✗（不是 D）
#     回溯到 C(0,2) → 换方向 F(1,2)✗ → 到底
#     最终找到路径：A→B→C→C→E→D→E ✓
#
# 时间复杂度：O(m × n × 3^L)——每个起点最多三个方向（不走回头路），L 为单词长度
# 空间复杂度：O(L)——递归栈深度 = 单词长度

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            """从 board[r][c] 出发，搜索 word[i:] 是否能匹配"""
            # 全部字符匹配完成 → 找到！
            if i == len(word):
                return True

            # 越界 或 当前格不匹配 → 死路
            if (r < 0 or r >= rows or c < 0 or c >= cols  # 修：c < 0 而非 c < cols
                    or board[r][c] != word[i]):
                return False

            # 标记当前格为"已访问"（原地修改，省掉 visited 集合）
            temp = board[r][c]
            board[r][c] = "#"  # 用特殊字符占位，保证不会重复走到

            # 向四个方向递归搜索下一个字符
            found = (dfs(r + 1, c, i + 1)   # 下
                     or dfs(r - 1, c, i + 1)  # 上
                     or dfs(r, c + 1, i + 1)  # 右
                     or dfs(r, c - 1, i + 1)) # 左

            # 回溯！恢复当前格，让其他路径能正常使用
            board[r][c] = temp

            return found

        # 尝试以每个格子为起点
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False
