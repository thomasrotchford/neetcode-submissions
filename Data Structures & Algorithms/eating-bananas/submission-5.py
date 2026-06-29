class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l=1
        r=max(piles)
        
        sol=0

        while l<=r:

            rate=((r-l)//2)+l

            hours=0

            for i in range(len(piles)):
                
                hours+=(piles[i]+rate-1)//rate

            if hours>h:
               l=rate+1

            elif hours<=h:
                sol=rate
                r=rate-1

            
        return sol


        