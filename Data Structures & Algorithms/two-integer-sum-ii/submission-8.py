class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
         
        l = 0
        r = len(numbers)-1

        while l < r:

            m = numbers[l]+numbers[r]

            if m < target:
                l+=1

                while numbers[l]==numbers[l-1]:
                    l+=1

            elif m > target:
                r-=1
                
                while numbers[r]==numbers[r+1]:
                    r-=1
            
            else:
                return [l+1,r+1]


