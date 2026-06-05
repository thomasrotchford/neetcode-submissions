class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dick={}

        for x in range(len(s)):

            if s[x] in dick:
                dick[s[x]]=dick[s[x]]+1
            else:
                dick[s[x]]=1
        
        for x in range(len(t)):
            
            if t[x] in dick:
                dick[t[x]]=dick[t[x]]-1

                if dick[t[x]]==0:
                    del dick[t[x]]
            else:
                return False       
        return not dick