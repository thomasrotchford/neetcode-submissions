class Solution:
    def isPalindrome(self, s: str) -> bool:

        left=0
        right=len(s)-1

        while left<right:

            if (ord(s[left].lower()) >= ord('a') and ord(s[left].lower()) <= ord('z')) == (ord(s[left]) >= ord('0') and ord(s[left]) <= ord('9')):
                print(left)
                left +=1
            
            elif (ord(s[right].lower()) >= ord('a') and ord(s[right].lower()) <= ord('z')) == (ord(s[right]) >= ord('0') and ord(s[right]) <= ord('9')):
                print(right)
                right -=1            

            elif s[left].lower() != s[right].lower():
                return False
            else:
                left+=1
                right-=1

        return True

            



        