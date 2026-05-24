class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Method 1: HashMap 
        # Time: O(n), Space: O(n)
        # d = {}
        # res, maxCount = nums[0], 1
        # for n in nums:
        #     d[n] = d.get(n, 0) + 1
        #     if d[n] > maxCount:
        #         res = n
        #         maxCount = d[n]
        # return res

        # Method 2: Boyer-Moore Voting Algo
        # Makes use of the fact that a majority elem exists 
        # and occurs more than half the input len
        # only specific inputs where majority elem occurs > n/2 will work for this alg
        # Time: O(n), Space: O(1)
        res, count = 0, 0
        for n in nums:
            if count == 0:
                res = n
            count += (1 if res == n else -1)
        return res 