class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #got feedback and hints on my last submission which was successful in passing neetcode but wasnt correct
        #focus on l,m,r and finding the target in the rotated array


        l=0
        r=len(nums)-1

        while l<=r:
            m=((r-l)//2)+l
            #if t is center of array
            if nums[m] == target:
                return m

            #if left half is sorted 
            elif nums[l] < nums[m]: #once entire subarray is sorted all loops will default to this if statement if target hasnt been found
                #and target is in it
                if nums[l] <= target < nums[m]:
                    #eliminate unsorted part
                    r = m-1

                #else target is in unsorted right half
                else:
                    #eliminate sorted half
                    #keep searching for sorted subarray with target
                    l = m+1

            #else right is sorted
            else:
                #and target in it                 
                if nums[m] < target <= nums[r]:
                    #eliminate unsorted part
                    l = m+1

                #edge case where subarray is on char long but is on right so m is in other array because of floor int divison, this does not need to exist if the left half is sorted but would speed it up by c time at cost of c memory
                elif target == nums[r]:
                    return r
                
                #target is in unsorted left half
                else:
                    #eliminate sorted half
                    #keep searching for sorted subarray with target
                    r = m-1

        #target does not exist
        return -1

