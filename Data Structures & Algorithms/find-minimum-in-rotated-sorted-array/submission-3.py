class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l=0
        r=len(nums)-1

        while l <= r:

            m = ((r-l)//2)+l

            if nums[l] <= nums[m] <= nums[r]:
                return nums[l] 
            
            #min is right of m
            elif nums[m] > nums[r]:
                l = m+1

            #min is left of m or is m
            else:
                r = m