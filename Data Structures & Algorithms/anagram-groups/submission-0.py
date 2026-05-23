class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # constraint: strs[i] is made up of lowercase English letters.
        # --> each str is made of 26 unique letters 
        # anagrams have the same count of each char

        # Time: O(m*n), where m is the number of strs and n is the len of longest str
        # Space: O(m), each str having its own character count, zero anagrams

        d = defaultdict(list)
        for s in strs:
            count = [0 for i in range(26)] # array of 26 zeroes
            # incremented based on idx of char in s i.e. if 'a' -> (val @ idx 0)  + 1
            for c in s:
                count[ord(c)-ord('a')] +=1
            d[tuple(count)].append(s)
        return list(d.values())