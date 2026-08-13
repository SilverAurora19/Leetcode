# LeetCode 155: 最小栈 (Min Stack)
#
# 题目：设计一个栈，支持 push/pop/top 之外，还能 O(1) 获取栈中最小值。
#
# 核心思路（辅助栈 / 双栈同步）：
# 用一个额外的 min_stack，与主栈 stack 同步增删。
# min_stack 的栈顶始终是"当前 stack 中的最小值"。
#
#   push 时：stack 压入 value，min_stack 压入 min(value, 当前最小值)
#   pop 时：两个栈同步弹出，保证 min_stack 栈顶仍对应 stack 剩余部分的最小值
#
# 这样 getMin 只需要返回 min_stack 栈顶，O(1)。
#
# 例如：依次 push 3, 2, 5, 1
#   stack:      [3]  [3,2]  [3,2,5]  [3,2,5,1]
#   min_stack:  [3]  [3,2]  [3,2,2]  [3,2,2,1]
#                               ↑ 5>2 所以仍存 2    ↑ 1<2 所以存 1
#
#   此时 getMin() → min_stack 栈顶 = 1 ✓
#   pop() → stack 弹出 1，min_stack 也弹出 1
#   getMin() → min_stack 栈顶 = 2 ✓（3,2,5 中最小是 2）
#
# 时间复杂度：所有操作 O(1)
# 空间复杂度：O(n)——两个栈各存 n 个元素

class MinStack:

    def __init__(self):
        self.stack = []        # 主栈，存所有元素
        self.min_stack = []    # 辅助栈，存"到当前位置为止的最小值"

    def push(self, value: int) -> None:
        self.stack.append(value)

        if not self.min_stack:
            # 辅助栈为空 → 第一个元素直接入栈
            self.min_stack.append(value)
        else:
            # 辅助栈压入 min(新值, 当前最小值)，保持栈顶是最小值
            self.min_stack.append(min(value, self.min_stack[-1]))

    def pop(self) -> None:
        # 两个栈同步弹出，保证 min_stack 栈顶始终对应 stack 的最小值
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        # 返回主栈栈顶元素
        return self.stack[-1]

    def getMin(self) -> int:
        # 返回辅助栈栈顶，即当前最小值
        return self.min_stack[-1]
