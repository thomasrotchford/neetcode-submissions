class Solution:
    def isPalindrome(self, s: str) -> bool:

        s=s.lower()
        alphaNum="abcdefghijklmnopqrstuvwxyz0123456789"

        startInd=0

        endInd=len(s)-1
        
        while startInd < endInd:
            if s[startInd] not in alphaNum:
                startInd=startInd+1
                continue
            
            if s[endInd] not in alphaNum:
                endInd=endInd-1
                continue

            
            if s[startInd]!=s[endInd]:
                return False
            
            startInd += 1
            endInd -= 1
        
        return True