class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #this solution will be better
        #still havent looked at a solution
        #asked chatgpt for improvement to my approach without giving me any code
        #it told me to keep the window a fixxed size
        #so i am rewriting

        if len(s2)<len(s1):
            return False
            


        l=0
        r=len(s1)-1
        permutation = defaultdict(int)
        for c in s1:
            permutation[c]+=1
        #build window of size len(s1)
        window = defaultdict(int)


    
        for i in range(len(s1)):
            window[s2[i]]+=1

        if window == permutation:
            return True

        #iterate the window through the rest of the string
        while r<len(s2)-1:
            
            window[s2[l]]-=1
            if window[s2[l]] <= 0:
                del window[s2[l]]
            l+=1 
            r+=1
            window[s2[r]]+=1
            if window == permutation:
                return True
            

        return False

            


            