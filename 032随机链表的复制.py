# LeetCode 138: 随机链表的复制 (Copy List with Random Pointer)
#
# 核心思路（哈希表映射，两次遍历）：
# 每个节点有两个指针：next（指向下一个）和 random（随机指向任意节点或 None）。
# 难点：复制时 random 指向的节点可能还没创建出来。
#
# 解法：用字典 old_to_new 建立"原节点 → 新节点"的映射关系。
#   第1趟：遍历原链表，为每个原节点创建一个新节点（只复制 val），存入字典。
#   第2趟：再次遍历原链表，通过字典查出对应的新 next 和新 random，完成连线。
#
# 字典初始化为 {None: None}，优雅处理了 next/random 为 None 的情况。
#
# 时间复杂度：O(n)，两次遍历
# 空间复杂度：O(n)，哈希表存 n 个映射

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node | None
        :rtype: Node | None   # 深拷贝后的链表头
        """
        if head is None:
            return None

        # 字典：原节点 → 对应的新节点
        # 初始化 {None: None}：处理 next 或 random 为 None 时直接返回 None
        old_to_new = {None: None}

        # 第1趟：克隆所有节点（只赋值 val，next 和 random 暂不管）
        current = head
        while current is not None:
            old_to_new[current] = Node(current.val)   # 创建新节点，仅复制值
            current = current.next

        # 第2趟：为新节点装配 next 和 random 指针
        current = head
        while current is not None:
            copied_node = old_to_new[current]               # 取出当前节点对应的新节点

            copied_node.next = old_to_new[current.next]     # 装配 next 指针
            copied_node.random = old_to_new[current.random] # 装配 random 指针

            current = current.next

        # 返回新链表的头节点
        return old_to_new[head]
