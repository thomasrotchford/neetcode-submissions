class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #got feedback and hints on my last submission which was successful in passing neetcode but wasnt correct
        #focus on l,m,r and finding the target in the rotated array
        #update: changed line 18 from < to <= since this catches case where l=m but nums[m]!= target, ie [X,Target]

        l=0
        r=len(nums)-1
        #loop invariant: valid range
        #inner loop logic: keep target in range
        while l<=r:
            m=((r-l)//2)+l
            #if t is center of array
            if nums[m] == target:
                return m

            #if left half is sorted 
            elif nums[l] <= nums[m]: #once entire subarray is sorted all loops will default to this if statement if target hasnt been found
                #and target is in it
                if nums[l] <= target < nums[m]:
                    #eliminate unsorted part
                    r = m-1

                #else target is in unsorted right half
                else:
                    #eliminate sorted half
                    l = m+1

            #else right is sorted
            else:
                #and target in it                 
                if nums[m] < target <= nums[r]:
                    #eliminate unsorted part
                    l = m+1
                
                #target is in unsorted left half
                else:
                    #eliminate sorted half
                    r = m-1

        #target does not exist
        return -1

