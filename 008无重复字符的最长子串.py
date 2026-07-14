# 核心思路：用 left 和 right 表示一个连续窗口；右指针不断加入新字符，一旦出现重复字符，就移动左指针，直到窗口重新变成“没有重复字符”。
# 右指针加入新字符；如果字符重复，就不断移动左指针，直到窗口重新无重复。
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        window_char = set()
        max_lens = 0
        left = 0

        for right in range(len(s)):
            while s[right] in window_char:
                window_char.remove(s[left])
                left += 1

            window_char.add(s[right])

            current_lens = right - left + 1
            max_lens = max(max_lens,current_lens)

        return max_lens