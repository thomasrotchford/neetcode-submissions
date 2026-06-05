class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dick={}

        for x in range(len(nums)):

            if nums[x] in dick:
                return True
            else:
                dick[nums[x]]=1

        return False
        