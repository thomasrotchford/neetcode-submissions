class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l=1

        r=max(piles)

        sol=0

        while l<=r:

            m=((r-l)//2)+l
            summ=0
            for num in piles:
                
                summ+=((num+m-1)//m)
            
            if summ<=h:
                sol=m
                r=m-1
            elif summ>h:
                l=m+1
        return sol
            
                
        