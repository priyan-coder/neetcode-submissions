class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # given nums, where len(nums) == n 
        
        ans = [1 for i in range(2*len(nums))]
        # Method 1: 
        # for i in range(len(ans)):
        #     ans[i] = nums[i % len(nums)]
        # return ans

        # Method 2: 
        n = len(nums)
        for i in range(n):
            ans[i] = ans[i + n] = nums[i]
        return ans