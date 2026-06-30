class Solution:
    def isValid(self, s: str) -> bool:
        
        stack=[]

        for i in range(len(s)):

            if s[i] in ['(','{','['] or not stack :
                stack.append(s[i])
            
            else:
            
                if ord(stack[-1])-ord('}')==ord('{')-ord(s[i]):
                    del stack[-1]

                elif ord(stack[-1])-ord(')')==ord('(')-ord(s[i]):
                    del stack[-1]

                elif ord(stack[-1])-ord(']')==ord('[')-ord(s[i]):
                    del stack[-1]
                    
                else:
                    return False


                
        return not stack