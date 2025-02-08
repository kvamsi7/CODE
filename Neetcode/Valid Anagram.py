''' 242. Valid Anagram 
    https://leetcode.com/problems/valid-anagram/
'''

class Solution:

    # method 1 
    # def isAnagram(self, s: str, t: str) -> bool:
    #     s = sorted(s)
    #     t = sorted(t)
    #     if s==t:
    #         return True
    #     else:
    #         return False

    # method 2
    def prepareStrDict(self,s:str):
        str_dict = {}
        for let in s:
            str_dict[let] = str_dict.get(let,0)+1
        return str_dict


    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = self.prepareStrDict(s)
        t_dict = self.prepareStrDict(t)
        if s_dict == t_dict:
            return True
        else:
            return False

    # method 3
    # def isAnagram(self, s:str, t: str) -> bool:
    #     t_list = list(t)
    #     if len(s) == len(t):
    #         for let in s:
    #             if let in t_list:
    #                 t_list.remove(let)
    #         if len(t_list) == 0:
    #             return True
    #         else:
    #             return False
    #     else:
    #         return False

sol = Solution()
print(sol.isAnagram("rat", "cat"))