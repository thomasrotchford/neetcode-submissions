class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def checkHours(piles, bPerH):

            hours=0

            for index in range(len(piles)):
                #ceiling division trick
                hours += -(piles[index]//-bPerH)

            return hours


        left=1
        right=max(piles)

        answer=0

        while left<=right:

            mid=(left+((right-left)//2))

            currentHours=checkHours(piles,mid)


            if currentHours<=h:
                answer=mid
                right=mid-1
            
            elif currentHours>h:
                left=mid+1
            
            


        return answer
