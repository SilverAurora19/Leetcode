# LeetCode 54: 螺旋矩阵 (Spiral Matrix)
#
# 核心思路（边界收缩法）：
# 用 top/bottom/left/right 四个边界不断向中心收缩。
# 每一轮按 上→右→下→左 的顺序遍历最外层，然后边界内缩一层。
#
# 例如 matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#   →  上：[1, 2, 3]
#   →  右：[6, 9]
#   →  下：[8, 7]
#   →  左：[4]
#   → 结果：[1, 2, 3, 6, 9, 8, 7, 4, 5]
#
# 注意：下侧遍历前需判断 top <= bottom，左侧遍历前需判断 left <= right，
#       防止只有一行或一列时重复遍历。
#
# 时间复杂度：O(rows × columns)
# 空间复杂度：O(1)（不计结果数组）

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]   # m×n 矩阵
        :rtype: List[int]               # 螺旋顺序的元素列表
        """
        rows = len(matrix)
        columns = len(matrix[0])

        # 四个边界，随着遍历逐步向中心收缩
        top = 0
        bottom = rows - 1
        left = 0
        right = columns - 1

        result = []

        # 只要上下边界和左右边界都没有交叉，就继续
        while top <= bottom and left <= right:

            # —— 1. 上边：从左到右 ——
            for column in range(left, right + 1):
                result.append(matrix[top][column])
            top += 1  # 上边界下移一行

            # —— 2. 右边：从上到下 ——
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1  # 右边界左移一列

            # —— 3. 下边：从右到左 ——
            # 需要再次判断 top <= bottom，防止在只有一行的情况下重复遍历
            if top <= bottom:
                for column in range(right, left - 1, -1):
                    result.append(matrix[bottom][column])
                bottom -= 1  # 下边界上移一行

            # —— 4. 左边：从下到上 ——
            # 需要再次判断 left <= right，防止在只有一列的情况下重复遍历
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1  # 左边界右移一列

        return result
