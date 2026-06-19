class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        sol=[0]*len(nums)

        before=[0]*len(nums)
        before[0]=1

        after=[0]*len(nums)
        after[-1]=1

        for i in range(1,len(nums)):
            before[i]=before[i-1]*nums[i-1]

        for i in range(len(nums)-2,-1,-1):
            after[i] = after[i+1]*nums[i+1]
        
        for i in range(len(nums)):
            sol[i]=before[i]*after[i]
        
        print(before)
        print(after)

        
        return sol