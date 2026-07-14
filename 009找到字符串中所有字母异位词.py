# 异位词长度相同、字符频率相同；固定窗口每次右移，只让一个字符进入、一个字符离开。
class Solution(object):
    def findAnagrams(self, s, p):
        """
        找到字符串 s 中所有 p 的字母异位词的起始索引。
        字母异位词：由相同字母以不同顺序组成的字符串。

        思路：滑动窗口 + 字符频率统计
        使用两个长度为 26 的数组分别记录 p 的字符频率和当前窗口的字符频率，
        窗口大小固定为 len(p)，每次滑动时更新频率数组，若相等则找到一个异位词。
        """
        # 如果 p 比 s 还长，不可能存在异位词
        if len(p) > len(s):
            return []

        window_size = len(p)               # 窗口大小 = p 的长度
        p_count = [0] * 26                 # 记录 p 中每个字母的出现次数
        window_count = [0] * 26            # 记录当前窗口中每个字母的出现次数

        # 初始化：统计第一个窗口的字符频率
        for index in range(window_size):
            p_char_index = ord(p[index]) - ord("a")   # p 中当前字符在字母表中的位置 (0~25)
            s_char_index = ord(s[index]) - ord("a")   # s 中当前字符在字母表中的位置 (0~25)

            p_count[p_char_index] += 1
            window_count[s_char_index] += 1

        result = []  # 存储所有异位词起始索引

        # 检查第一个窗口是否为异位词
        if window_count == p:
            result.append(0)

        # 滑动窗口：right 为窗口的右边界
        for right in range(window_size, len(s)):
            incoming_index = ord(s[right]) - ord("a")                        # 进入窗口的字符
            outgoing_index = ord(s[right - window_size]) - ord("a")          # 离开窗口的字符

            # 更新窗口频率：加入新字符，移除旧字符
            window_count[incoming_index] += 1
            window_count[outgoing_index] -= 1

            # 若当前窗口频率与 p 的频率一致，记录起始索引
            if window_count == p_count:
                start = right - window_size + 1  # 窗口起始位置
                result.append(start)

        return result