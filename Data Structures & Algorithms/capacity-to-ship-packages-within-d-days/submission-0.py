class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #if days given == len(weights). smallest possible
        l = max(weights)
        #weight required if only one day given. largest possible
        r = max(weights)*len(weights)

        solution = r
        

        while l<=r:
            m = ((r-l)//2)+l
            print("Max capacity: ", m)
            time = 0  
            sumWeights = 0
            #enforce order of string
            for weight in weights:
                if sumWeights + weight > m:
                    sumWeights = weight
                    time+=1
                elif sumWeights + weight == m:
                    sumWeights = 0
                    time+=1
                else:
                    sumWeights+=weight
            if sumWeights > 0:
                time+=1
            if time <= days:
                solution=min(solution,m)
                r=m-1
            else:
                l=m+1

        return solution
        