from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        for num in nums:
            count_map[num] = count_map.get(num,0) + 1
        topFreqNums  = list(dict(sorted(count_map.items(),key=lambda x:x[1],reverse=True)).keys())
        return topFreqNums[:k]


sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3],2))

        
