class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        solution = 0
        
        # Char : last index seen
        allChar = {}

        l = 0
        
        for r in range(len(s)) :
            
            frontChar = s[r]

            if frontChar in allChar :
                lastSeen = allChar[frontChar]

                if lastSeen >= l:
                    l = lastSeen + 1

                allChar[frontChar] = r

            else:
                allChar[frontChar] = r

            solution = max(solution, r-l+1)

        return solution
            

        






        