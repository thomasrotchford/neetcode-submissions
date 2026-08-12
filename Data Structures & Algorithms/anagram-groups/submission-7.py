class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anaDict = {}

        for s in strs:
            characteristic = [0] * 26
            
            for c in s:
                characteristic[ord(c) - ord("a")] += 1
                
            charT = tuple(characteristic)

            if charT in anaDict:
                anaDict[charT].append(s)

            else:
                anaDict[charT] = [s]

        solution = []

        for k, v in anaDict.items():
            solution.append(v)

        return solution
