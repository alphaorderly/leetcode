# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        self.arr = []

        def inorder(node: TreeNode):
            if not node:
                return 

            inorder(node.left)
            self.arr.append(node)
            inorder(node.right)

        inorder(root)

        for i in range(len(self.arr)):
            if self.arr[i].val == p.val:
                if i == len(self.arr) - 1:
                    return None
                else:
                    return self.arr[i + 1]
