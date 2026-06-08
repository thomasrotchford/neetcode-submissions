class Solution:
    def arrangeCoins(self, n: int) -> int:

        def calcN(q):
            return q*(q+1)*0.5     



        left=0



        right=n

        while left<=right :

            mid=(left+right)//2

            N=calcN(mid)

            if N==n:
                return mid

            elif N>n:
                if left==mid:
                    return mid-1
                else:
                    right=mid-1

            elif N<n:
                if right==mid:
                    return mid
                else:
                    left=mid+1





            
        
