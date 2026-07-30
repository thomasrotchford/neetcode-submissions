class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0

        solution = 0

        lastSeen = defaultdict()

        for r in range(len(s)):

            if s[r] in lastSeen and lastSeen[s[r]] >= l:
                l = lastSeen[s[r]] + 1

            lastSeen[s[r]] = r
            
            solution = max(solution, r-l+1, 1)

        return solution