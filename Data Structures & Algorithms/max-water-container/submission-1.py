class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        #two scenarios
        #move smaller bound inward
        #  1: next bound is the same, new area = width-1 *height
        #  2: next bound it bigger but still smaller than other bound, new area = width-1 *height+x where x>=1
        l = 0
        r = len(heights)-1
        solution = 0

        while l < r:
            
            area = min(heights[l],heights[r]) * (r-l)

            solution = max(solution, area)

            if heights[l] <= heights[r]:
                l+=1
            elif heights[r] < heights[l]:
                r-=1

        return solution
            
        