class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1

        #l<r not <= because one number cannot be used twice
        while l<r:

            sum=numbers[l]+numbers[r]

            if sum>target:
                r-=1
            elif sum<target:
                l+=1
            else:
                return [l+1,r+1]
            
        #problem wants index starting at 1, this throws me off alot
        #no return here because problem states there will always be a solution