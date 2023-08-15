class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        x = sorted(nums)
        p = 1
        for n in x:
            if n == p:
                p += 1
            elif n > p:
                return p
        return p
