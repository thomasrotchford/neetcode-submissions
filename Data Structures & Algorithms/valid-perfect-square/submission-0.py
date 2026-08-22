class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        l = 1
        r = num

        while l <= r:
            m = ((r-l)//2)+l

            square = m*m

            if square == num:
                return True
            
            elif square < num:
                l = m+1

            else:
                r = m-1

        return False