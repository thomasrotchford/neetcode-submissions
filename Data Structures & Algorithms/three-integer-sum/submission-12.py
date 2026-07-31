class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        solution = []
        strLen = len(nums)-1

        for i in range(len(nums)):

            if nums[i] > 0:
                break
            
            if i > 0 and nums[i-1] == nums[i]:
                i+=1
                continue

            l = i+1
            r = strLen
            dumbBool = True
            while l < r:
                sum = nums[i] + nums[l] + nums[r]

                if sum < 0:
                    l+=1

                elif sum > 0:
                    r-=1

                else:
                    solution.append([nums[i], nums[l], nums[r]])
                    #last submission was incorrect but neetcode sub checks were inadequate
                    r-=1
                    while l<r and nums[r+1] == nums[r]:
                        r-=1

                    l+=1
                    while l<r and nums[l-1] == nums[l]:
                        l+=1

        return solution