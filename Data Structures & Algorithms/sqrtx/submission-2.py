class Solution:
    def mySqrt(self, x: int) -> int:

        l = 0
        r = x
        saved = -1

        while l <= r:
            m = ((r-l)//2)+l

            sqrt = m*m

            if sqrt > x:
                r = m-1

            elif sqrt < x:
                l = m+1
                saved = m
            
            else:
                return m
        return  saved
        