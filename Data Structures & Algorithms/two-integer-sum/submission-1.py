class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = []
        for i in range(len(nums)):
            needed = target - nums[i]
            if needed in seen:
                num = seen.index(needed)
                return [num,i]
            else:
                seen.append(nums[i])
        return [0,0]