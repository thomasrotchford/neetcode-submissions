class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        solution = r
        while l <= r :
            rate = ((r-l)//2)+l

            hours = 0

            for pile in piles:
                #int division with ceiling instead of floor
                hours += ((pile+rate-1)//rate)

            #solution found
            #save and search for potential better solution
            #make next rate slower
            if hours <= h:
                solution = min(solution, rate)
                r = rate-1

            #not a valid solution, rate must be higher
            elif hours > h:
                l = rate+1
            
        
        return solution
        