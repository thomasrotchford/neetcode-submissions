class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sol = []

        anaDic = {}

        for str in strs:

            temp=[0]*26

            for char in str:

                temp[ord('z')-ord(char)]+=1

            if tuple(temp) in anaDic:

                anaDic[tuple(temp)].append(str)

            else:

                anaDic[tuple(temp)] = [str]

        for key,val in anaDic.items():

            sol.append(val)

        return sol

        