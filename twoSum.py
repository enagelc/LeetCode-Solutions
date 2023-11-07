class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen_nums = {}

        for i, num in enumerate(nums):
            if target - num in seen_nums:
                return [i, seen_nums[target-num]]
            seen_nums[num] = i

        return [-1]