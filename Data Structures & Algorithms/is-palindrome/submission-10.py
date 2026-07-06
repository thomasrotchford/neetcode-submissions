class Solution:
    def isPalindrome(self, s: str) -> bool:

        l=0
        r=len(s)-1

        alNum={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9'}
        s=s.lower()
        while l<len(s)-1 and r>=0:


            while l<len(s)-1 and s[l] not in alNum:
                
                l+=1


            while r>=0 and s[r] not in alNum:
                r-=1

            if s[l]!=s[r] and s[l] in alNum and s[r] in alNum:
                return False

            l+=1
            r-=1

        return True
        