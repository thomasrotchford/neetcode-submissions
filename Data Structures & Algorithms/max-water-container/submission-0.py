class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left=0

        right=len(heights)-1

        maxArea=0
        #< because no area if equal
        while left<right:

            area = (right-left)*min(heights[left],heights[right])

            if heights[left]<=heights[right]:
                left+=1
            elif heights[left]>heights[right]:
                right-=1

            maxArea=max(maxArea,area)
        return maxArea





            

