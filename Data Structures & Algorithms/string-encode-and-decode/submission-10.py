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

        ind=0

        while ind < len(s):

            if s[ind]==";":
                decoded_string.append("")
                decoded_string[wordInd]=s[ind+1:ind+int(leng)+1]
                ind=ind+int(leng)
                wordInd=wordInd+1
                leng=""
            else:
                leng=leng+s[ind]
            ind=ind+1
                

        
        return decoded_string
