class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        all_nums = sorted(nums1 + nums2)
        if len(all_nums) % 2 == 0:
            return ((all_nums[len(all_nums)//2] + all_nums[len(all_nums)//2 - 1]) /2)
        else:
            return all_nums[len(all_nums)//2]
