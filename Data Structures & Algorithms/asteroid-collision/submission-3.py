class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for asteroid in asteroids:

            #stack empty
            if not stack:
                stack.append(asteroid)

            #collision
            elif asteroid < 0 and stack[-1] > 0:
                
                #pop all lesser stack vals
                while stack and stack[-1] > 0 and abs(asteroid) > abs(stack[-1]):
                    stack.pop()

                #asteroid was greater than all stack vals
                if not stack or stack[-1]<0:
                    stack.append(asteroid)

                #if same pop stack and do not append
                elif stack[-1] == asteroid*-1:
                    stack.pop()

                #else asteroid found one bigger than it, dont add

            #same direction
            else:
                stack.append(asteroid)



        return stack