'''
487. Max Consecutive Ones II
Author: kvamsi7
'''
class Solution:
    ## brute force 
    # def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

    #     max_c = 0
    #     for i in range(len(nums)):
    #         zero_c = 1
    #         one_c = 0
    #         for j in range(i,len(nums)):
    #             if nums[j] == 1:
    #                 one_c += 1
    #             elif nums[j] == 0:
    #                 if zero_c > 0:
    #                     one_c += 1
    #                     zero_c -= 1
    #                 else:
    #                     break
    #         i += 1
    #         if max_c < one_c:
    #             max_c = one_c
    #     return max_c

    # T(n) -> O(n)
    # Sliding Window
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest_sequence = 0
        left, right = 0, 0
        zeros_c = 0

        while right < len(nums):
            if nums[right] == 0:
                zeros_c += 1
                
            
            while zeros_c == 2:
                if nums[left] == 0:
                    zeros_c -= 1
                left += 1
            
            longest_sequence = max(right - left+1,longest_sequence)
            right += 1
        return longest_sequence
        