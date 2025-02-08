'''@11. Container With Most Water
   author: kvamsi7
'''

class Solution:
    def get_area(self,start,end,height):
        length = min(height[start],height[end])
        width = end - start
        return length * width

    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1
        max_water = 0

        while start < end:
            water = self.get_area(start,end,height)
            if water > max_water:
                max_water = water

            if height[start] < height[end]:
                start += 1
            elif height[start] > height[end]:
                end -= 1
            else:
                start += 1
                end -= 1
        return max_water

