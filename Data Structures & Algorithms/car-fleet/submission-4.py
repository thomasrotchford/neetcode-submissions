class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack=[float("inf")]

        sol = 0

        ps = zip(position,speed)
        ps = sorted(ps, key=lambda ps : ps[0])

        for p,s in ps:
            travelTime = (target-p)/s
            
            while travelTime >= stack[-1]:
                stack.pop()

            stack.append(travelTime)

        return len(stack)-1