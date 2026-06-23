class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #almost did by myself 
        #mistakes i made: 
        #incrementing pointers by binary search amount
        #not having a default return value
        left=0

        right=len(numbers)-1

        while left<right:

            if numbers[left]+numbers[right] < target:
                left=left+1
            
            elif numbers[left]+numbers[right] > target:
                right=right-1

            else:
                return [left+1,right+1]
            
        return []