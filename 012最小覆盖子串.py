# LeetCode 76: 最小覆盖子串 (Minimum Window Substring)
# 核心过程：右指针扩张窗口，直到包含 t 的全部字符；然后左指针收缩窗口，直到再缩一步就不满足要求。
# 右边扩张直到覆盖目标，左边收缩直到即将失效；合法窗口中不断更新最短答案。
class Solution(object):
    def minWindow(self, s, t):
        """
        找出 s 中包含 t 所有字符的最短子串。

        思路：滑动窗口 + 哈希表
        - need：记录 t 中每个字符的需求数量
        - window_count：记录当前窗口中字符的统计数量
        - matched_chars：当前窗口中有多少个字符"满足需求"（不重复计多出的部分）
          （例如 t = "AA"，窗口中有一个 A 时 matched_chars = 1，两个 A 时 matched_chars = 2 = len(t)）
        右指针不断右移扩张窗口，当窗口覆盖 t 后（matched_chars == len(t)），
        左指针右移尝试缩小窗口，直到不再满足，期间记录最短窗口。
        """
        # 边界情况：s 太短或 t 为空，无解
        if not t or not s or len(t) > len(s):
            return ""

        # 统计 t 中每个字符的需求量
        need = {}
        for char in t:
            if char in need:
                need[char] += 1
            else:
                need[char] = 1

        window_count = {}    # 当前窗口中各字符的出现次数
        matched_chars = 0    # 当前窗口中已"达标"的字符个数（≤ len(t)）

        left = 0             # 窗口左指针

        best_start = 0       # 当前最优窗口的起始下标
        best_length = len(s) + 1  # 当前最优窗口的长度，初始化为不可能的大值

        for right in range(len(s)):     # right 为窗口右指针，逐步右移
            right_char = s[right]

            # 只关心 t 中需要的字符（无关字符直接忽略）
            if right_char in need:
                # 将当前字符计入窗口
                if right_char in window_count:
                    window_count[right_char] += 1
                else:
                    window_count[right_char] = 1

                # 如果该字符在窗口中的数量尚未超过需求量，
                # 说明它"贡献"了一次有效匹配，matched_chars 加 1
                if window_count[right_char] <= need[right_char]:
                    matched_chars += 1

            # 当窗口已覆盖 t 中所有字符时，尝试收缩左边界
            while matched_chars == len(t):
                current_length = right - left + 1

                # 如果当前窗口更短，更新最优解
                if current_length < best_length:
                    best_start = left
                    best_length = current_length

                left_char = s[left]  # 即将被移出窗口的字符

                if left_char in need:
                    window_count[left_char] -= 1

                    # 移除后若窗口中的数量低于需求，
                    # 说明窗口不再满足要求，matched_chars 减 1
                    if window_count[left_char] < need[left_char]:
                        matched_chars -= 1

                left += 1  # 收缩左边界

        # 如果 best_length 没被更新过，说明没有满足条件的窗口
        if best_length == len(s) + 1:
            return ""

        return s[best_start:best_start + best_length]

