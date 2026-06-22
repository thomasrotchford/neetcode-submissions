class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #review and redo for understanding

        #remove last index of pre and first of postfix to save memory
        #since the product of all numbers is never needed
        prefix=[1]*(len(nums)-1)

        postfix=[1]*(len(nums)-1)

        sol=[0]*len(nums)

        prefix[0]=nums[0]
        for index in range(1,len(prefix)):
            prefix[index]=nums[index]*prefix[index-1]
        print(prefix)
        
        postfix[len(postfix)-1]=nums[len(nums)-1]
        for index in range(len(postfix)-2,-1,-1):
            postfix[index]=nums[index+1]*postfix[index+1]
        print(postfix)

        sol[0]=postfix[0]
        sol[len(sol)-1]=prefix[len(prefix)-1]
        for index in range(0,len(sol)-2):
            sol[index+1]=prefix[index]*postfix[index+1]
        
        return sol

        