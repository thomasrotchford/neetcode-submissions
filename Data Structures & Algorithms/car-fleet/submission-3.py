class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        #all positions are unique
        pos2arrival = {} 

        for p,s in zip(position, speed):
            pos2arrival[p] = ((target-p)/s)
        
        pos2arrival = sorted(pos2arrival.items(), key=lambda pos2arrival: pos2arrival[0], reverse=True)
        #print(pos2arrival)

        sol = 0
        prev = -1

        for positionOfCar,arrivalTime in pos2arrival:
            #arriving later than last on stack could be the start of a fleet, assign new group #
            if prev < arrivalTime:
                sol+=1
                prev = arrivalTime #update previous to next slowest
            
        return sol
                


