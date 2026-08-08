# LeetCode 105: 从前序与中序遍历序列构造二叉树
# (Construct Binary Tree from Preorder and Inorder Traversal)
#
# 前置知识：
#   前序：根 → 左 → 右（第一个元素一定是整棵树的根）
#   中序：左 → 根 → 右（根把数组分成左右两半：左边全是左子树，右边全是右子树）
#
# 核心思路（递归 + 哈希表）：
# 1. 前序的第一个元素是当前子树的根。
# 2. 在中序里找到这个根的位置，左边就是左子树的中序，右边是右子树的的中序。
# 3. 递归构造左右子树。
#
# 前序的作用：告诉每一层"谁是根"
# 中序的作用：告诉每一层"左右子树的范围"
# 哈希表的作用：O(1) 在中序中查根的位置
#
# 例如：preorder = [3, 9, 20, 15, 7]
#        inorder  = [9, 3, 15, 20, 7]
#
#   preorder[0]=3 是整棵树的根 → 在中序找到 3 在 idx=1
#   中序被切分为：左=[9]  右=[15,20,7]
#   对应前序：    左=[9]  右=[20,15,7]（对应的前序段）
#
#   递归：
#     左子树：preorder 下一个是 9 → 根=9, 中序中位置=0 → 左右都空 → 叶子
#     右子树：preorder 下一个是 20 → 根=20, 中序中位置=0（在右半段中）
#            → 左=[15] 右=[7] → ...
#
# 时间复杂度：O(n)——每个节点建一次，哈希查位置 O(1)
# 空间复杂度：O(n)——哈希表 + 递归栈

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode | None
        """
        self.preorder_index = 0  # 前序数组的全局指针，每次取一个就是当前的根

        # 哈希表：值 → 在中序数组中的下标，O(1) 查根的位置
        inorder_index = {}
        for index, value in enumerate(inorder):
            inorder_index[value] = index

        def build(inorder_left, inorder_right):
            """递归构造中序数组中 [left..right] 区间对应的子树"""
            # 区间无效 → 空子树
            if inorder_left > inorder_right:
                return None

            # 前序的下一个元素就是当前子树的根值
            root_value = preorder[self.preorder_index]
            self.preorder_index += 1               # 全局指针前移，准备下一次取

            root = TreeNode(root_value)

            # 在中序中找到根的位置，划分左右子树范围
            middle = inorder_index[root_value]

            # 左子树：中序的 [inorder_left, middle - 1]
            root.left = build(inorder_left, middle - 1)
            # 右子树：中序的 [middle + 1, inorder_right]
            root.right = build(middle + 1, inorder_right)

            return root

        # 初始区间：整个中序数组
        return build(0, len(inorder) - 1)
