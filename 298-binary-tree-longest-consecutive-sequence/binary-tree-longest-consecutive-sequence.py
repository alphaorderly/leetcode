class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        checked = set()

        def check(node: Optional[TreeNode]):
            if node in checked:
                return max(check(node.left), check(node.right))

            if not node:
                return 0

            s = [(node, 1)]

            checked.add(node)

            max_value = 1

            while s:
                p, d = s.pop()

                checked.add(p)

                max_value = max(max_value, d)

                if p.left and p.left.val == p.val + 1:
                    s.append((p.left, d + 1))

                if p.right and p.right.val == p.val + 1:
                    s.append((p.right, d + 1))

            return max(max_value, check(node.left), check(node.right))

        return check(root)