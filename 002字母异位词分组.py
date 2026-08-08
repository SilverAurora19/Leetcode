# 核心思路（排序 + 字典分组）：
# 字母异位词排序后得到的字符串完全相同（如 "eat" 和 "tea" 排序后都是 "aet"）。
# 因此用排序后的字符串作为字典键，将原字符串归入同一组。
#
# 时间复杂度：O(n·k log k)，n 为单词数，k 为单词平均长度（排序开销）
# 空间复杂度：O(n·k)

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]        # 单词列表
        :rtype: List[List[str]]      # 按异位词分组后的列表
        """
        groups = {}  # 键：排序后的字符串；值：原单词列表

        for word in strs:
            # sorted(word) 返回一个排序后的字符列表，如 ['a', 'e', 't']
            # "".join(...) 将其拼回字符串，作为分组的键
            key = "".join(sorted(word))

            # 首次出现该键 → 创建空列表
            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())  # 返回字典所有值（即分组后的列表）
