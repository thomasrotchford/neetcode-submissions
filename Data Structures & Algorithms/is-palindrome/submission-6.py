class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l=0
        r=len(s)-1

        s=s.lower()

        alphaNum={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9'}

        while l<r:
            while l<r and s[l] not in alphaNum:
                l+=1
                
            
            while r>l and s[r] not in alphaNum:
                r-=1

            
            if s[r]!=s[l]:
                return False
            
            l+=1
            r-=1

        return True