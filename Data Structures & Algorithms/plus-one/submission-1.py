class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        index = len(digits) - 1
        
        while digits[index] == 9:

            digits[index] = 0
            index -= 1

        match index:
            case -1:
                return [1] + digits

            case _:
                digits[index] += 1
                return digits
