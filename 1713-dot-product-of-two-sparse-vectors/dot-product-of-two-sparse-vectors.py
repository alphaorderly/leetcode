class SparseVector:
    def __init__(self, nums: List[int]):
        self.save = dict()
        for i, v in enumerate(nums):
            self.save[i] = v

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        for i, v in vec.save.items():
            if i not in self.save:
                continue
            else:
                ans += v * self.save[i]
        return ans

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)