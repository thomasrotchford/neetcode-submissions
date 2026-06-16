class Solution:
    ##numdelimword
    def encode(self, strs: List[str]) -> str:

        encoded_string=[]

        for word in strs:
            encoded_string.append(str(len(word)))
            encoded_string.append(";")
            encoded_string.append(word)


        return "".join(encoded_string)

    def decode(self, s: str) -> List[str]:

        decoded_string=[]

        wordInd=0

        leng=""

        ADD=False

        for ind in range(len(s)):


            if not ADD and ord(s[ind])>=ord('0') and ord(s[ind])<=ord('9'):
                leng=leng+s[ind]
            elif s[ind]==";":
                ADD=True
                counter=int(leng)
                
                decoded_string.append("")
                decoded_string[wordInd]=s[ind+1:ind+int(leng)+1]
                wordInd=wordInd+1
                leng=""
            if ADD:
                if counter==0:
                    ADD=False
                counter=counter-1
                

        
        return decoded_string
