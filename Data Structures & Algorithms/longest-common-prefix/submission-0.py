class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Time: Outer loop only runs while chars match in the shortest str of len n
        #     : we iterate across m strings -> O(n*m)
        # Space: O(1)

        # column by column scan across the strs
        # going through each char of the first str & then compare across all other strs
        for i in range(len(strs[0])):
            for s in strs:
                # either we don't have enough chars in the susbsequent strs to keep 
                # going or chars dont match 
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0] # all letters of the first string matched as prefix 