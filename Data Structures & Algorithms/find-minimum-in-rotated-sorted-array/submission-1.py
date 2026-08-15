class Solution:
    def findMin(self, nums: List[int]) -> int:
        #solved bsearch in rotated array before this, so i imagine that will help
        #hints used: None, only given problem type (bsearch)
        #first attempt was 8/10
        #hint given to me was to change my return case
        #revised my elimination cases and found one already included a way to return a solution

        l=0
        r=len(nums)-1

        while l<=r:
            m=((r-l)//2)+l

            #min is right of center
            if nums[m] > nums[r]:
                l=m+1
            
            #min is left of center or on center so cant always lose m
            elif nums[m] < nums[r]:
                r=m
            
            #min is on center
            else:
                return nums[m]
        
        #there will always be a min value