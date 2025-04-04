# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def deepest(node: TreeNode):
            if not node:
                return -1
            if not node.left and not node.right:
                return 1

            return 1 + max(deepest(node.left), deepest(node.right))

        def deepestCount(node: TreeNode, target: int, level: int):
            if not node:
                return []
            if level == target:
                return [node.val]

            return deepestCount(node.left, target, level + 1) + deepestCount(node.right, target, level + 1)

        lvl = deepest(root)

        cnt = deepestCount(root, lvl, 1)

        if len(cnt) == 1:
            return TreeNode(cnt[0])

        s = len(cnt)

        print(lvl, cnt)

        target = None

        def findRoot(node: TreeNode, level: int):
            nonlocal target, s, lvl
            if not node:
                return 0
            if not node.left and not node.right and level == lvl:
                return level

            current = findRoot(node.left, level + 1) + findRoot(node.right, level + 1)
            if current == lvl * s and target is None:
                target = node

            return current

        findRoot(root, 1)
            
        return target