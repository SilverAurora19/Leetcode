# LeetCode 131: 分割回文串 (Palindrome Partitioning)
#
# 题目：把字符串 s 分割成若干子串，要求每个子串都是回文串。
# 返回所有可能的分割方案。
#
# 核心思路（回溯 + 剪枝）：
# 用回溯（backtrack）在字符串上"切"回文子串。
#   从 start 位置开始，尝试所有可能的 end（start ~ len(s)-1）：
#   - 如果 s[start..end] 是回文 → 切下来加入 path，递归处理剩下的
#   - 如果不是回文 → 跳过（剪枝）
#   递归到底（start == len(s)）→ 找到一种方案，加入结果。
#
# 回溯的核心：每次只关心"第一刀切哪儿"，剩下的交给递归。
#
# 例如：s = "aab"
#
#   start=0: end=0→"a"是回文 → path=["a"], 处理"ab"
#     start=1: end=1→"a"是回文 → path=["a","a"], 处理"b"
#       start=2: end=2→"b"是回文 → path=["a","a","b"], 处理空 ✓方案1
#     start=1: end=2→"ab"不是回文 → 跳过
#     ← 回溯，path=["a"]
#   start=0: end=1→"aa"是回文 → path=["aa"], 处理"b"
#     start=2: end=2→"b"是回文 → path=["aa","b"], 处理空 ✓方案2
#   start=0: end=2→"aab"不是回文 → 跳过
#
#   结果：[["a","a","b"], ["aa","b"]]
#
# 时间复杂度：O(n × 2^n)——最坏情况下每个字符间都可以切或不切
# 空间复杂度：O(n)——递归栈深度 + path 长度

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]   # 所有可能的分割方案
        """
        res = []   # 存放所有合法分割方案
        path = []  # 当前正在构造的分割方案（一条路径）

        def is_palindrome(left, right):
            """判断 s[left..right] 是否为回文串"""
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start):
            """从 s[start:] 开始分割，构造合法方案"""
            # start 走到了字符串末尾 → 所有字符都切完了 → 记录方案
            if start == len(s):
                res.append(path.copy())  # copy() 因为 path 后面会被修改
                return

            # 尝试以 end 为"第一刀终点"的所有可能
            for end in range(start, len(s)):
                # 如果当前子串不是回文 → 跳过（剪枝）
                if not is_palindrome(start, end):
                    continue

                # 是回文 → 切下来，加入 path
                path.append(s[start:end + 1])

                # 递归处理剩余部分
                backtrack(end + 1)

                # 回溯：撤销这次切割，尝试下一种切法
                path.pop()

        backtrack(0)
        return res
