# 字母异位词排序后相同，因此用排序后的字符串作为字典键，将原字符串加入对应列表。
class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}

        for word in strs:
            key = "".join(sorted(word))      # sorted() 可以处理字符串等可迭代对象，并返回一个新的列表。

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())

   