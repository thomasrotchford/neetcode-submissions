class Solution:
    def trap(self, height: List[int]) -> int:

        l = 0
        r = len(height)-1

        maxl = 0
        maxr = 0

        summ = 0

        while l<r:
            heightl = height[l]
            heightr = height[r]

            if heightl < heightr:

                l+=1
                maxl = max(heightl,maxl)
                summ += maxl - heightl 
                
            else:
        
                r-=1
                maxr = max(heightr,maxr)
                summ += maxr - heightr

        return summ