class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        save=nums[0]

        for index in range(1,len(nums)):
            save= nums[index]^save
        return save

        