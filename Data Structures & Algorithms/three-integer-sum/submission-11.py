class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        solution = []
        rTracker = len(nums)-1

        for i in range(len(nums)):

            if nums[i] > 0:
                break
            
            if i > 0 and nums[i-1] == nums[i]:
                i+=1
                continue

            l = i+1
            r = rTracker
            dumbBool = True
            print("OUTER: ",l,r)
            while l < r:
                print("INNER: ",l,r)
                sum = nums[i] + nums[l] + nums[r]

                if sum < 0:
                    l+=1

                elif sum > 0:
                    r-=1

                else:
                    print("SOLUTION: ",l,r)
                    solution.append([nums[i], nums[l], nums[r]])

                    #minor improvement, now if the mag of r is greater than the other 2 combined (-2,-2,4)
                    # it will not be included in the next search because 
                    # it couldnt possibly create a new trip equal to zero
                    # now r must skip dupes here too
                    #the idea is now every inner loop (while l<r) r values that are too large are checked fewer times
                    if nums[r] < abs(nums[i]) + abs(nums[l]):
                        r = len(nums) - 1
                    else:
                        if r == len(nums)-1:
                            r-=1
                        else:
                            while l<r and nums[r] == nums[r+1]:
                                r-=1

                    #minor improvement #2 bring first lower r to outside
                    # to prevent this calculation above from running multiple times
                    # it only stores the first result since that one is 
                    if dumbBool:
                        rTracker = r
                        dumBool = False
                    
                    #end minor improvement

                    l+=1
                    while l<r and nums[l-1] == nums[l]:
                        l+=1

        return solution