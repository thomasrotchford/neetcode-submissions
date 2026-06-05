class Solution:
    def isValid(self, s: str) -> bool:
        stack1=[] #()


        if len(s)==0 or len(s)%2==1:
            return False
        for x in range(len(s)):
            
            if s[x]== "(" :
                stack1.append("(")

            elif s[x]== "[" :
                stack1.append("[")

            elif s[x]== "{" :
                stack1.append("{")  

            elif s[x]== ")" and len(stack1) != 0 and stack1[-1]=="(":
                stack1=stack1[:-1]

            elif s[x]== "]" and len(stack1) != 0 and stack1[-1]=="[":
                stack1=stack1[:-1]

            elif s[x]== "}" and len(stack1) != 0  and stack1[-1]=="{":
                stack1=stack1[:-1]
            else:
                return False

        if len(stack1)==0:
            return True
        else:
            return False