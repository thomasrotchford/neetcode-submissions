class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)

        #baller dictionary comprehension again
        dick = { num:[num] for num in nums if num-1 not in numSet }

        sol = 0
        for key,val in dick.items():

            d = 1
            while key + d in numSet:

                val.append(key + d)

                d+=1
            
            if sol < len(val) :

                sol = len(val)
        
        return sol
        