# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        checked = set()

        ans = 1

        def check(node: Optional[TreeNode]):
            nonlocal ans

            if node in checked:
                check(node.left)
                check(node.right)
                return

            if not node:
                return

            s = [(node, 1)]

            checked.add(node)

            while s:
                p, d = s.pop()

                checked.add(p)

                ans = max(ans, d)

                if p.left and p.left.val == p.val + 1:
                    s.append((p.left, d + 1))

                if p.right and p.right.val == p.val + 1:
                    s.append((p.right, d + 1))

            check(node.left)
            check(node.right)

            return

        check(root)

        return ans