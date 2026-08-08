# LeetCode 438: 找到字符串中所有字母异位词 (Find All Anagrams in a String)
#
# 字母异位词：两个字符串包含的字母种类和个数完全相同，只是顺序不同。
# 如 "abc" 和 "bca" 互为异位词。
#
# 核心思路（固定窗口滑动 + 频率数组）：
# 既然异位词只关心字母频率、不关心顺序，就用两个长度为 26 的数组分别统计 p 的频率和当前窗口中每个字母的频率。
# 窗口大小 = len(p)，每次右移一格：一个新字母进来，一个旧字母出去。
# 如果两个频率数组完全相等，说明当前窗口是一个异位词。
#
# 为什么不用排序比较？
#   排序每个窗口 O(k log k)，n 个窗口总 O(n·k log k)；
#   频率数组每次只改两个位置 O(1)，总 O(n)，快很多。
#
# 例如：s = "cbaebabacd", p = "abc"（len=3）
#   p 频率：  a=1, b=1, c=1
#   窗口[0:3]："cba" → c=1,b=1,a=1 == p → 记录 idx=0
#   窗口[1:4]："bae" → b=1,a=1,e=1 ≠ p（e多了,c少了）
#   窗口[2:5]："aeb" → 不对
#   窗口[3:6]："eba" → 不对
#   窗口[4:7]："bab" → 不对
#   窗口[5:8]："aba" → 不对
#   窗口[6:9]："bac" → b=1,a=1,c=1 == p → 记录 idx=6
#   结果：[0, 6]
#
# 时间复杂度：O(n)——只需遍历一次
# 空间复杂度：O(1)——两个固定大小 26 的数组

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str   # 源字符串
        :type p: str   # 目标模式
        :rtype: List[int]   # 所有异位词在 s 中的起始索引
        """
        if len(p) > len(s):
            return []

        window_size = len(p)               # 窗口大小固定 = p 的长度
        p_count = [0] * 26                 # p 中每个字母的出现频率（字母 a~z → 索引 0~25）
        window_count = [0] * 26            # 当前窗口中每个字母的出现频率

        # 第1步：初始化，统计 p 和第一个窗口的字符频率
        for index in range(window_size):
            # ord(char) - ord("a")：把字母映射到 0~25
            p_count[ord(p[index]) - ord("a")] += 1
            window_count[ord(s[index]) - ord("a")] += 1

        result = []

        # 第一个窗口单独判断
        if window_count == p_count:
            result.append(0)

        # 第2步：滑动窗口，右边界从 window_size 开始
        for right in range(window_size, len(s)):
            # 计算"进入窗口"和"离开窗口"的字符索引
            incoming = ord(s[right]) - ord("a")                     # 右边进来的新字符
            outgoing = ord(s[right - window_size]) - ord("a")       # 左边滑出的旧字符

            # 更新窗口频率：进一出一，只改两处，O(1)
            window_count[incoming] += 1
            window_count[outgoing] -= 1

            # 频率数组完全相同 → 当前窗口就是异位词
            if window_count == p_count:
                start = right - window_size + 1       # 窗口的起始下标
                result.append(start)

        return result
