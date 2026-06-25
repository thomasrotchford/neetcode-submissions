class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #attempt to make O(1) memory
        
        left=1
        right=max(piles)

        answer=0

        while left<=right:

            currentHours=0
            mid=(left+((right-left)//2))
            
            for index in range(len(piles)):
                #ceiling division trick
                currentHours += -(piles[index]//-mid)




            if currentHours<=h:
                answer=mid
                right=mid-1
            
            elif currentHours>h:
                left=mid+1
            
            


        return answer
