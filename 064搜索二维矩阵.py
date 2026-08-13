# LeetCode 74: 搜索二维矩阵 (Search a 2D Matrix)
#
# 题目特性：每一行递增，且每行第一个元素 > 上一行最后一个元素。
# 这意味着整个矩阵如果按行展开，是一个严格递增的一维数组。
#
# 核心思路（一次二分查找）：
# 把矩阵"想象"成一个长度为 rows × cols 的一维有序数组：
#   下标 mid → 矩阵中的 (row, col) = (mid // cols, mid % cols)
#   然后就是标准的二分查找。
#
# 区别于 021（搜索二维矩阵 II）：
#   021 的矩阵只是"行内递增 + 列内递增"，不能展开为一维；
#   本题矩阵每行之间严格有序，可以直接二分。
#
# 例如：matrix = [[1, 3, 5, 7],
#                  [10,11,16,20],
#                  [23,30,34,60]], target = 3
#   展开：[1,3,5,7,10,11,16,20,23,30,34,60]  共 12 个元素
#   二分：mid=5 → (5//4, 5%4) = (1,1) → 值=11 > 3 → 缩右边
#         mid=2 → (2//4, 2%4) = (0,2) → 值=5 > 3 → 缩右边
#         mid=0 → (0//4, 0%4) = (0,0) → 值=1 < 3 → 缩左边
#         mid=1 → (1//4, 1%4) = (0,1) → 值=3 == 3 → 找到！
#
# 时间复杂度：O(log(mn))
# 空间复杂度：O(1)

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols - 1    # 修：rows * cols - 1（不是 rows * right - 1）

        # 标准二分查找，闭区间 [left, right]
        while left <= right:
            mid = (left + right) // 2

            # 把一维下标转换为二维坐标
            r = mid // cols          # 行号 = mid ÷ 列数
            c = mid % cols           # 列号 = mid 除以列数的余数
            value = matrix[r][c]

            if value == target:
                return True
            elif value < target:
                left = mid + 1       # 目标在右半区
            else:
                right = mid - 1      # 目标在左半区

        return False
