# LeetCode 394: 字符串解码 (Decode String)
#
# 题目：解码形如 "3[a2[c]]" 的字符串，规则是 k[encoded_string] 表示把括号内内容重复 k 次。
# 例如："3[a2[c]]" → "accaccacc"
#
# 核心思路（栈）：
# 用栈处理嵌套结构。维护两个变量：
#   cur_str：当前正在构建的字符串
#   cur_num：当前正在读取的数字
#
# 遇到不同字符：
#   数字  → 累加到 cur_num（注意多位数字，如 "12"）
#   '['   → 把当前的 cur_str 和 cur_num 压栈，然后清空，进入新的嵌套层
#   ']'   → 弹栈取出之前的字符串和重复次数，把当前字符串重复后接回去
#   字母  → 追加到 cur_str
#
# 例如：s = "3[a2[c]]"
#   3        → cur_num=3
#   '['      → 压栈 ("", 3)，清空 cur_str/cur_num
#   a        → cur_str="a"
#   2        → cur_num=2
#   '['      → 压栈 ("a", 2)，清空
#   c        → cur_str="c"
#   ']'      → 弹 ("a",2)，cur_str = "a" + "c"*2 = "acc"
#   ']'      → 弹 ("",3)，cur_str = "" + "acc"*3 = "accaccacc"
#   返回 "accaccacc"
#
# 时间复杂度：O(n)——每个字符处理一次（字符串拼接的复制总开销也是 O(输出长度)）
# 空间复杂度：O(n)——栈的深度

class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str   # 解码后的字符串
        """
        stack = []        # 栈，存 (进入嵌套前的字符串, 重复次数)
        cur_num = 0       # 当前正在读取的数字
        cur_str = ""      # 当前正在构建的字符串

        for char in s:
            if char.isdigit():
                # 是数字：处理多位数字，如 "12" → 1*10 + 2
                cur_num = cur_num * 10 + int(char)

            elif char == '[':
                # 进入新的一层嵌套：把当前状态压栈保存，然后清空
                stack.append((cur_str, cur_num))
                cur_num = 0
                cur_str = ""

            elif char == ']':
                # 结束一层嵌套：弹出之前保存的状态
                pre_str, repeat = stack.pop()
                # 当前字符串重复 repeat 次，接到之前的字符串后面
                cur_str = pre_str + cur_str * repeat

            else:
                # 是字母：直接追加到当前字符串
                cur_str += char

        return cur_str
