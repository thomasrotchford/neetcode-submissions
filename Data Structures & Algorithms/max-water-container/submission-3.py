class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights)-1
        sol = 0

        while l<r :
            
            sol = max(sol,min(heights[l],heights[r])*(r-l))
            if heights[l] > heights[r]:

                r-=1

            elif heights[r] > heights[l]:

                l+=1

            else:
                
                if (r-l)%2 == 0:
                    l+=1 

                else:
                    r-=1

        return sol
