class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet=set(nums)
        
        sequences={}
        sol=0
        
        for num in numSet:
            
            if num-1 not in numSet:

                sequences[num]=[num]
        

        for num in numSet:  

            if num-1 in sequences:
                
                #append num
                sequences[num-1].append(num)
                #and update key to num
                sequences |= {num-1:sequences[num-1]}

                leng=1
                #needed help to get this while loop
                while num + leng in numSet:

                    sequences[num-1].append(num+leng)

                    leng+=1




        for k,v in sequences.items():
            if len(v)>sol:
                sol=len(v)
        print(numSet)
        print(sequences)    
        return sol
            

            
                


        