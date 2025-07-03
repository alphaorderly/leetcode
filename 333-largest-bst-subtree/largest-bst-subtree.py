from collections import defaultdict
from typing import Optional

# Provided TreeNode class for context
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        count = defaultdict(int)

        def count_size(node: Optional[TreeNode]):
            if not node:
                return 0

            count[node] += 1 + count_size(node.left) + count_size(node.right)

            return count[node]

        count_size(root)

        ans = 0

        def check_bst(node: Optional[TreeNode]):

            nonlocal ans

            if not node:
                return True, float('inf'), -float('inf')

            left_is_bst, left_min, left_max = check_bst(node.left)
            right_is_bst, right_min, right_max = check_bst(node.right)

            if left_is_bst and right_is_bst and left_max < node.val < right_min:
                ans = max(ans, count[node])
                return True, min(left_min, node.val), max(right_max, node.val)
            
            return False, 0, 0

        check_bst(root)

        return ans