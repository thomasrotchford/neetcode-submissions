class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        dick={}

        numSet=set(nums)

        #Add all beginings to dick
        
        for num in numSet:
            
            if num-1 not in numSet:
                dick[num]=[num]
                
                l=1
                while num+l in numSet:
                    dick[num].append(num+l)
                    l+=1
        #find longest
        sol=0
        for key,value in dick.items():
            if len(value)>sol:
                sol=len(value)   
        return sol
