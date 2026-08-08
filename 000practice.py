class Solution(object):
    def inorderTraversal_1(self, root):
        result = []

        def inorder(node):
            if node is None:
                return
            
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)

        return result

    def inorderTraversal_2(self, root):
        result = []
        stack = []
        current = root

        while current is not None or stack:
            while current is not None:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.val)

            current = current.right

        return result
