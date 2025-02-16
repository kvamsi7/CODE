'''
3066. Minimum Operations to Exceed Threshold Value II
Author: kvamsi7
'''
import heapq
class Solution:

    ## brute force T(n) = n * nlogn
    # def minOperations(self, nums: List[int], k: int) -> int:
    #     nums.sort()
    #     count = 0
    #     while (len(nums) > 1):
    #         if nums[0] < k:
    #             nums.append(min(nums[0],nums[1]) * 2 + max(nums[0],nums[1]))
    #             nums = nums[2:]
    #             nums.sort()
    #             count += 1
    #         else:
    #             break
    #     return count

    ## using priority queue, T(n) = O(n logn) + O(1) or O(logn)
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        count = 0
        while len(nums) > 1:
            min1 = heapq.heappop(nums)
            min2 = heapq.heappop(nums)
            if min1 < k:
                val = min(min1,min2) * 2 + max(min1,min2)
                heapq.heappush(nums,val)
                count += 1
            else:
                break
        return count

"""
[2,11,10,1,3], k = 10
[1,2,3,10,11]
 ^
   ^
"""


        