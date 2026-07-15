class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        d={}

        for num in nums:

            if num not in d:

                d[num]=1
            
            else:

                d[num]+=1

        sol=0
        freq=0
        for key,val in d.items():

            if val>freq:

                sol=key
                freq=val
        
        return sol
        