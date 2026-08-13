class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqDict = {}

        for num in nums:
            if num in freqDict:
                freqDict[num]+=1
            else:
                freqDict[num]=1
        
        freqBuckets = [[] for i in range(len(nums)+1)]

        for key, value in freqDict.items():
            freqBuckets[value].append(key)

        solution = []*k
        for i in range(len(freqBuckets)-1,-1,-1):
            for j in range(len(freqBuckets[i])-1,-1,-1):
                solution.append(freqBuckets[i][j])
                if len(solution) == k:
                    return solution
        


        