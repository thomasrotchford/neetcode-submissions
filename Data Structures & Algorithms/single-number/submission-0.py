class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        answer = 0

        for x in range(len(nums)):
            answer = nums[x] ^ answer
        print(answer)
        return answer
        