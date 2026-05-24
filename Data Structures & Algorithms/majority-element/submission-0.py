class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Method 1: HashMap 
        # Time: O(n), Space: O(n)
        d = {}
        res, maxCount = nums[0], 1
        for n in nums:
            d[n] = d.get(n, 0) + 1
            if d[n] > maxCount:
                res = n
                maxCount = d[n]
        return res