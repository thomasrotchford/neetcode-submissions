class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #review and redo for understanding

        prefix=[1]*len(nums)

        postfix=[1]*len(nums)

        sol=[0]*len(nums)

        prefix[0]=nums[0]
        for index in range(1,len(nums)):
            prefix[index]=nums[index]*prefix[index-1]
        #print(prefix)
        
        postfix[len(postfix)-1]=nums[len(nums)-1]
        for index in range(len(postfix)-2,-1,-1):
            postfix[index]=nums[index]*postfix[index+1]
        #print(postfix)

        sol[0]=postfix[1]
        sol[len(sol)-1]=prefix[len(prefix)-2]
        for index in range(1,len(sol)-1):
            sol[index]=prefix[index-1]*postfix[index+1]
        
        return sol

        