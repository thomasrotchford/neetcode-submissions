class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = [[float("inf"),-1]] #[value, index]
        solution = [0]*len(temperatures) #backfill with 0s

        for i,temp in enumerate(temperatures):

            while stack[-1][0] < temp: #resolve temps looking for a greater temp
                tt = stack.pop(-1) #remove from stack
                solution[tt[1]] = i - tt[1] #calc their days

            stack.append([temp,i])#push new value
   
        return solution
               