class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        f={}

        for num in nums:

            if num in f:
                f[num]+=1
            else:
                f[num]=1

        #+1 beceause a list could be full of one element to its frequency would be equal to len(nums) which would index ob
        a=[[] for i in range(len(nums)+1)]
        for key,v in f.items():
            a[v].append(key)

        kArr=[]
        for i in range(len(a)-1,0,-1):

            for j in a[i]:

                
                kArr.append(j)

                if len(kArr)==k:
                    return kArr



        
        


        