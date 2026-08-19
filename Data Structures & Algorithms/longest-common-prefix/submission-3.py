class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs)==1:
            return strs[0]
        sol=strs[0]

        for str1 in strs[1:]:
            temp=[]
            for c in range(min(len(sol),len(str1))):
                if sol[c] == str1[c]:
                    temp.append(sol[c])
                else:
                    break
            if temp:
                sol = temp
            else:
                return ""
        return "".join(sol) if sol != strs[0] else ""