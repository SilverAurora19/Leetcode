# 核心思路（滑动窗口 + 集合判重）：
# 用 left 和 right 维护一个不含重复字符的连续窗口。
# right 不断向右扩张，当新字符与窗口内重复时，left 右移并移除字符，
# 直到窗口重新无重复。
#
# 时间复杂度：O(n)
# 空间复杂度：O(k)，k 为字符集大小

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int   # 最长无重复子串的长度
        """
        window_char = set()  # 当前窗口中的字符集合，用于 O(1) 判重
        max_lens = 0          # 全局最长无重复子串长度
        left = 0              # 窗口左边界

        for right in range(len(s)):
            # 如果新字符已在窗口中，收缩左边界，直到重复字符被移除
            while s[right] in window_char:
                window_char.remove(s[left])
                left += 1

            # 将新字符加入窗口
            window_char.add(s[right])

            # 更新最大长度
            current_lens = right - left + 1
            max_lens = max(max_lens, current_lens)

        return max_lens
