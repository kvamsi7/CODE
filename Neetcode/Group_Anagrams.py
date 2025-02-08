from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        count = [0] * 26
        for s in strs:
            for c in s:
                count[ord(c) - ord("a")] +=1
            res[tuple(count)].append(s)
            count = [0]*26
        return res.values()

    
sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))