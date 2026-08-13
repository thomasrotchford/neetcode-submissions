class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        window = {}
        solution = 0
        l = 0
        freq = 0

        for r, v in enumerate(s):

            if v in window:
                window[v]+=1
            else:
                window[v]=1
            
            freq = max(freq, window[v])

            while r-l+1-freq > k:

                window[s[l]]-=1
                l+=1
            solution = max(solution, r-l+1)
        return solution