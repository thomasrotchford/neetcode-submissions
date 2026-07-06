class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet=set(nums)
        #baller dict comprehension
        dick={num:[num] for num in nums if num-1 not in numSet}
        
        solution=0
        for num,v in dick.items():
            
            length=1
            while num in dick and num+length in numSet:

                dick[num].append(num+length)
                length+=1
            if num in dick and len(dick[num])>solution:
                solution=len(dick[num])
                
        print(dick)
        return solution
        

        