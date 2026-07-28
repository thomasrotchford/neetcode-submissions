class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        def twoSumSorted(target, arr):
            l = 0
            r = len(arr) -1
            while l < r:
                s = arr[l] + arr[r]
                if s < target :
                    l = l+1
                elif arr[l] + arr[r] > target :
                    r = r-1
                else:
                    return [arr[l],arr[r]]
            return None

        
        #no help atttempt 3 hints used

        nums = sorted(nums) 
        print(nums)
        
        # format i : j,k
        sol = []
        solSet = set()

        for i in range(len(nums)):
            numsMinus = [ num for num in nums]
            
            numsMinus.pop(i)
            
            rez = twoSumSorted(-1*nums[i], numsMinus)
            while rez: 
                numsMinus.remove(rez[0])
                numsMinus.remove(rez[1])
                rez.append(nums[i])
                sol.append(rez)
                rez = twoSumSorted(-1*nums[i], numsMinus)
                
        print(sol)
        for arr in sol:
            temp = tuple(sorted(arr))
            solSet.add(temp)
        
        return [list(num) for num in solSet]
