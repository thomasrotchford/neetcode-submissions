class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        answer={}

        for word in strs:

            key=[0]*26

            for chr in word:
                
                key[ord(chr)-ord('a')]=key[ord(chr)-ord('a')]+1

            if tuple(key) in answer:
                answer[tuple(key)].append(word)
            else:
                answer[tuple(key)]=[word]

        return list(answer.values())
        