class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        solution=0

        votes=0

        for num in nums:

            if votes == 0:
                solution = num
            
            if num == solution:

                votes+=1
            
            else:

                votes-=1
        
        return solution
        