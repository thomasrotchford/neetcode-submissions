class Solution:

    def encode(self, strs: List[str]) -> str:
        
        answer=[]
        for str1 in strs:
            answer.append(str(len(str1)))
            answer.append("&")
            answer.append(str1)
        
        return "".join(answer)

    def decode(self, s: str) -> List[str]:

        number=[]
        sol=[]
        i=0
        while i < len(s):

            if s[i] == "&":
                n=int("".join(number))
                sol.append(s[i+1:i+n+1])
                i+=(n+1)
                number.clear()
            else:
                number.append(s[i])
                i+=1
        
        return sol


            