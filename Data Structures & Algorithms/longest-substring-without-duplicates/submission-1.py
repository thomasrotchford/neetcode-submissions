class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        solution = 0

        allSeq = set()
        
        for startPtr in range(len(s)) :

            tempSeq = set()



            for i in range(startPtr,len(s)):

                if s[i] not in tempSeq:

                    tempSeq.add(s[i])
            
                else:
                    break
        
            startPtr += 1
        
            allSeq.add(tuple(tempSeq))
        
            solution = max(solution, len(tempSeq))

        return solution
            

        






        