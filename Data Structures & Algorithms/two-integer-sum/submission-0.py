class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dick={}
        answer=[]

        for x in range(len(nums)):

            if target-nums[x] in dick:
                return [dick[target-nums[x]],x]
            
            else:
                dick[nums[x]]=x
                
