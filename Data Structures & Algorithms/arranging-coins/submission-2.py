class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        answer=n

        for i in range(0,n):

            if (answer-(i))< i+1:
                return i
            elif (answer-(i))==i+1:
                return i+1
            else:
                answer=answer-i