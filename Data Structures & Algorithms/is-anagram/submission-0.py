class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagrams = same count of each char but jumbled up in diff order
        if len(s) != len(t):
            return False

        # both s and t have the same length but we need 
        # to check if they have the same count of each char
        
        d = {} # char: count_of_char
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0) + 1
        
        # check against t
        for i in range(len(t)):

            # case a: t has a char which occurs more times than in s 
            if t[i] not in d:
                return False
            
            # case b: both s and t have this char 
            d[t[i]] -=1
            if d[t[i]] == 0:
                d.pop(t[i])
            
        return len(d) == 0 # ensures all chars in s are accounted for 