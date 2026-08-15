class Solution:#currently no hints used
    def search(self, nums: List[int], target: int) -> int:
        def bSearch(arr: List[int], t: int) -> int:
            l=0
            r=len(arr)-1
            while l<=r:
                m=((r-l)//2)+l
                if arr[m]<t:
                    l=m+1
                elif arr[m]>t:
                    r=m-1
                else:
                    return m
            return -1
        
        
        unRotated = []
        left=0
        right=len(nums)-1
        offset=0

        #unrotated array
        if nums[left] < nums[((right-left)//2)+left] < nums[right] or len(nums)==1:
            return bSearch(nums,target)
        poop=0
        while left<=right and poop<5:
            middle=((right-left)//2)+left
            #print(left,middle,right)
            print(nums[left],nums[middle],nums[right])
            
            #length is short enough to contain continous start sequence
            if right-middle==1:
                #case 123
                if nums[left]<nums[middle]<nums[right]:
                    unRotated = nums[left:right+1]+nums[right+2:len(nums)-1]+nums[0:left]
                    offset=left

                #case x12
                elif nums[left]>=nums[middle]<nums[right]:
                    unRotated = nums[middle:right+1]+nums[right+2:len(nums)-1]+nums[0:middle]
                    offset=middle
                
                #case xx1
                elif nums[middle]>nums[right]:
                    unRotated = nums[right:len(nums)]+nums[0:right]
                    offset=right
                break

            #rotated less than len(nums)/2 times
            #start right of center
            elif nums[left] < nums[middle] > nums[right]:
                left = middle+1

            #rotated more than len(nums)/2 times
            #start left of center or at center
            elif nums[left] > nums[middle] < nums[right]:
                right = middle-1
            if nums[left]==target:
                return left
            elif nums[right]==target:
                return right
            elif nums[middle]==target:
                return middle
        #print(unRotated)
        sol = bSearch(unRotated,target)
        #print(sol)
        return (sol+offset)%len(nums) if sol!=-1 else -1






        
        