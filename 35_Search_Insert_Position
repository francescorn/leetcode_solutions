class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            for index, number in enumerate(nums):
                if target < number:
                    return nums.index(number)
            return len(nums)
