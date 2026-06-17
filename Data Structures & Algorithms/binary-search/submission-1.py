class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            midpoint=(r+l)//2
            
            if target==nums[midpoint]:
                return midpoint
            elif target<nums[midpoint]:
                r=midpoint-1
            elif target>nums[midpoint]:
                l=midpoint+1

        return -1
        