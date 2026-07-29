class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #review #3

        #sort array so that twosum with 2ptr can run on it
        nums = sorted(nums)
        print(nums)

        #array for solution triplets
        solution = []
        
        #last 2 digits cannot have a calculation for a triplet
        # i represents each potential fixed point
        for i in range(len(nums)-2):

            #if left ptr passes middle
            #remain values are pos and cannot be used to make a trip equal 0
            #cannot be ==0 because of cases with at least 3 0s
            if nums[i] > 0:
                break

            #after first loop
            #skip all duplicates to avoid overlapping computations
            #>=0 to make it skip dupe
            #edge case: [0,0,0,0]
            #the solution is found but the next outer loop skips i out of bounds
            #can be addressed by an "if continue" instead of a "while" to reeval outer loop condition to prevent failure
            if i > 0 and nums[i]==nums[i-1]:
                i+=1
                continue

            #delcare ptrs
            #l is i+1 because the range of the 2ptr search must not include the fixed value
            # and the current fixed val has already been included in searchs using the smaller
            # nums before it and those have been found so they(the fixed val and ones before it) cannot possibly
            # be needed in inner calculations
            l = i+1
            r = len(nums)-1

            #since indices selected must be unique l!=r, so l<r
            while l < r:
                #twoSum sorted calculation
                threeSum = nums[i] + nums[l] + nums[r]

                #if too small, increase the negative number
                if threeSum < 0:
                    l+=1

                #if too big decrease the positive number
                elif threeSum > 0:
                    r-=1
                
                else:
                    #solution found but do not exit, keep searching in the remaining range
                    solution.append([nums[i], nums[l], nums[r]])

                    #r has been used in current solution and possibly in one for the numbers greater than it
                    # so it passes out of the scope of the current search

                    #dupe values do not matter for r since eliminating the possibility of dupes
                    # for one of the 3 triplets eliminates the possibility of duped trips

                    #since one value is fixed and you only run one inner loop for that value
                    # and the two unfixed ones must relate to the fixed one (-fixed = unfixed1 + unfixed2)
                    # so if the right side has duplicate values (-4-2-1-1-10011222222222)
                    # they could only possibly sum to zero when used with one certain fixed value
                    # (-4,2,2) is the only true trip with (x,2,2)
                    # so long as we do not repeat the fixed value, the other vals can coexist in the calculation with no risk
                    # that being said, the values on the right could be skipped for greater efficiency
                    # since the nature of the sorted array is that once they are used they will not be used by the next (outer loop) calculation
                    r-=1
                    #progress for l if not a dupe
                    l+=1
                    #l has been used in current solution, if the next l is a dup
                    # it could lead to duplicate solution
                    while l < r and nums[l] == nums[l-1]:
                        l+=1


        return solution
        