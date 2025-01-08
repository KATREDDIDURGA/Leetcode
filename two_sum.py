class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = {}
        for i, num in enumerate(nums):
            z = target - num
            if z in x:
                return [x[z], i]
            x[num] = i
