class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        sol=[1]*len(nums)

        for index in range(len(nums)):
            for index2 in range(len(sol)):
                if index!=index2:
                    sol[index2]=sol[index2]*nums[index]
        
        return sol
        

        