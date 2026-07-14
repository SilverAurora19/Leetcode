# 面积由短边决定，宽度移动后一定变小，所以应该移动短边，寻找更高的边。
class Solution(object):
    def maxArea(self,height):
        left = 0
        right = len(height)- 1
        maxArea = 0

        while left < right:
            current_width = right - left
            current_height = min(height[left],height[right])
            current_area = current_height * current_width

            maxArea = max(maxArea,current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea


if __name__ == "__main__":
    s = Solution()
    tests = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),   # LeetCode 示例
        ([1, 1], 1),                            # 最小输入
        ([4, 3, 2, 1, 4], 16),                 # 两边高中间低
        ([1, 2, 1], 2),                         # 中间高两边低
        ([2, 3, 4, 5, 18, 17, 6], 17),         # 随机
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 20),    # 递增
        ([9, 8, 7, 6, 5, 4, 3, 2, 1], 20),    # 递减
        ([5, 5, 5, 5, 5], 20),                 # 全等
    ]

    all_pass = True
    for height, expected in tests:
        result = s.maxArea(height)
        status = "PASS" if result == expected else "FAIL"
        if result != expected:
            all_pass = False
        print(f"{status}: height={height} -> {result} (expected {expected})")

    print()
    if all_pass:
        print("All passed!")
    else:
        print("Some tests FAILED!")
