class Solution:
    def mySqrt(self, x: int) -> int:

        l=0
        r=x


        midpt=0

        save=0

        while l<=r:
            midpt=((r-l)//2)+l

            if midpt*midpt>x:
                r=midpt-1

            elif midpt*midpt<x:
                l=midpt+1
                save=midpt
            else:
                return midpt

        return save