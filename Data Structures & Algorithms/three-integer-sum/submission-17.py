class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        rightStart = len(nums) - 1

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = rightStart

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1

                elif total > 0:
                    right -= 1

                else:
                    result.append(
                        [nums[i], nums[left], nums[right]]
                    )
                    
                    if nums[right] != abs(nums[i]) + abs(nums[left]):
                        right = len(nums) - 1
                    elif right == len(nums) - 1:
                        right -= 1
                    else:
                        while (left < right and nums[right] == nums[right + 1]):
                            right -= 1

                    rightStart = right

                    left += 1
                    while ( left < right and nums[left] == nums[left - 1]):
                        left += 1

        return result