class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string=""

        for word in strs:
            encoded_string=encoded_string+word+";"
        return encoded_string

    def decode(self, s: str) -> List[str]:

        decoded_string=[""]*len(s)

        wordInd=0

        for char in s:

            if char==";":
                wordInd=wordInd+1
            else:
                decoded_string[wordInd]=decoded_string[wordInd]+char
            
        sol=decoded_string[:wordInd]
        

        return sol
