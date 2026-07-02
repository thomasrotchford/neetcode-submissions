class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d={}

        for num in nums:
            #at 0 for indexing to work
            if num not in d:
                d[num]=0
            else:
                d[num]+=1
        
        f=[[] for i in range(len(nums))]

        for key,val in d.items():
            f[val].append(key)
        
        solution=[]

        for arr in reversed(f):
            for ind in reversed(arr):
                
                if len(solution)==k:
                    break
                solution.append(ind)

        return solution


        