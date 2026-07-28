class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #review
        d = {}

        for i in range(len(nums)):

            diff = target - nums[i]

            if diff in d:

                return [d[diff],i]
            
            else:

                d[nums[i]] = i
