class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq={}
        freqArr=[[] for i in range(len(nums))]
        solution=[]

        for num in nums:
            #start at zero so freqArr can index at 0
            if num not in freq:
                freq[num]=0
            else:
                freq[num]+=1
        
        for key,value in freq.items():

            freqArr[value].append(key)



        for f in reversed(freqArr):
                
            for i in reversed(f):

                solution.append(i)
                
                if(len(solution)==k):
                    return solution



        