class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq=[[] for i in range(len(nums)+1)]
        sol=[]

        for i in range(len(nums)):

            if nums[i] in count:
                count[nums[i]]=count[nums[i]]+1

            else:
                count[nums[i]]=1

        for key, value in count.items():

            freq[value].append(key)

        for i in range(len(freq)-1,-1,-1):
            for j in range(len(freq[i])):


                sol.append(freq[i][j])
                
            if len(sol)==k:
                return sol

        

        