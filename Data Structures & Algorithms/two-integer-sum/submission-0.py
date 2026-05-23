class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # find two unique indices where the nums sum up to target
        # constraints: just one possible solution, len(nums) >= 2
        # Space : O(n)
        # Time: O(n), one pass
        
        seen = {} # value : idx
        for i in range(len(nums)):
            if (target - nums[i]) in seen:
                return [seen[target-nums[i]], i]  
            seen[nums[i]] = i