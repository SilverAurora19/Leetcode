# LeetCode 139: 单词拆分 (Word Break)
#
# 题目：判断字符串 s 能否被拆分成 wordDict 中若干单词的组合（单词可重复使用）。
#
# 核心思路（动态规划）：
# dp[i] = s 的前 i 个字符（s[0:i]）能否被成功拆分。
#
# 递推公式：
#   dp[i] = True，如果存在一个分割点 j（0 ≤ j < i），使得：
#     1. dp[j] 为 True（前 j 个字符能拆）
#     2. s[j:i] 是字典里的一个单词（剩下这段能直接匹配）
#
# 即：把 s[0:i] 切成"能拆的前半段 + 一个单词"。
#
# 初始：
#   dp[0] = True（空字符串视为可以拆分）
#
# 例如：s = "leetcode", wordDict = ["leet", "code"]
#   dp[0] = True
#   i=4："leet" → dp[0]=True 且 s[0:4]="leet" 在字典 → dp[4]=True
#   i=8："code" → dp[4]=True 且 s[4:8]="code" 在字典 → dp[8]=True
#   返回 dp[8] = True ✓
#
# 反例：s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
#   最终 dp[n] = False，因为无法拆分完整。
#
# 时间复杂度：O(n²)——两层循环
# 空间复杂度：O(n)——dp 数组

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool   # 能否拆分
        """
        word_set = set(wordDict)   # 转集合，O(1) 判断单词是否存在

        n = len(s)
        dp = [False] * (n + 1)     # dp[i] = s 前 i 个字符能否拆分
        dp[0] = True               # 空字符串可拆

        for i in range(1, n + 1):          # i 是当前考虑的结束位置
            for j in range(i):             # j 是分割点，把 s[0:i] 切成 s[0:j] 和 s[j:i]
                # 前半段能拆 且 后半段是字典里的单词 → 整体能拆
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break                  # 找到一种拆分即可，提前退出

        return dp[n]
