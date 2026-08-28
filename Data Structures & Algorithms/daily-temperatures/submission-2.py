class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = [[float("inf"),-1]] #[value, index]
        solution = [0]*len(temperatures) #backfill with 0s
        l = 0

        for i,temp in enumerate(temperatures):
            
            if temp > stack[-1][0]:
                while stack[-1][0] < temp:
                    tt = stack.pop(-1)
                    solution[tt[1]] = i - tt[1]

            stack.append([temp,i])
   

        return solution
               