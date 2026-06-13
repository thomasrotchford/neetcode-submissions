class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        dic={}

        for i in range(len(strs)):
            key=[0]*26
            for letter in strs[i]:
                key[ord(letter)-ord('a')]=key[ord(letter)-ord('a')]+1
            
            if tuple(key) in dic:
                dic[tuple(key)].append(strs[i])
            else:
                dic[tuple(key)]=[strs[i]]
        
        return list(dic.values())
        


        