class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Time : O(n)
        # Space: O(1)
        # At the end, everything before index k contains valid elements.
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i] # non val num replaces num at k 
                k +=1 # move k forward 
        return k        