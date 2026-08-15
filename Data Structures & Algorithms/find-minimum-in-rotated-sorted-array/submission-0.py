class Solution:
    def findMin(self, nums: List[int]) -> int:
        #solved bsearch in rotated array before this, so i imagine that will help
        #hints used: None, only given problem type (bsearch)

        l=0
        r=len(nums)-1

        while l<=r:
            m=((r-l)//2)+l

            #3 or less char left
            if r-l+1 <= 3:
                #[1] [1,2] [3,1,2]
                if nums[l] >= nums[m] <= nums[r]:
                    return nums[m]
                #[2,1] [2,3,1]
                elif nums[l] <= nums[m]> nums[r]:
                    return nums[r]
                #[1,2,3]
                elif nums[l] < nums[m] <= nums[r]:
                    return nums[l]    
            #min is right of center
            elif nums[l] < nums[m] > nums[r]:
                l=m+1
            
            #min is right of center or is on center
            else:
                r=m
        
        #there will always be a min value