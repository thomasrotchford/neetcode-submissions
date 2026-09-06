class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = [[float("inf"),-1]]

        sol = [0]*len(temperatures)

        for i,temp in enumerate(temperatures):

            while temp > stack[-1][0]:
                poppedTemp = stack.pop()
                sol[poppedTemp[1]] = i - poppedTemp[1]

            stack.append([temp,i])

        return sol


        