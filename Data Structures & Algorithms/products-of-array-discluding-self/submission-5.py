class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        grow=[1]*len(nums)
        shrink=[1]*len(nums)
        solution=[1]*len(nums)

        grow[0]=nums[0]
        for i in range(1,len(nums)):

            grow[i]=grow[i-1]*nums[i]
        
        shrink[-1]=nums[-1]
        for i in range(len(nums)-2,-1,-1):

            shrink[i]=shrink[i+1]*nums[i]

        solution[0]=shrink[1]
        solution[-1]=grow[-2]
        for i in range(1,len(nums)-1):

            solution[i]=grow[i-1]*shrink[i+1]

        return solution
