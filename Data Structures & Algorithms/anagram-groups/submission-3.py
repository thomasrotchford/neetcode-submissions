class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def makeDict(string):

            dic = {}

            for i in range(len(string)):
                if string[i] in dic:
                    dic[string[i]] = dic[string[i]] + 1

                else:
                    dic[string[i]] = 1

            return dic

        # sort by length? to make index time shorter?
        strs = sorted(strs)

        answers = []

        for index in range(len(strs)):
            if len(strs) != 0:
                length = len(strs[0])
                # make characteristic dictionary
                dicky = makeDict(strs[0])

                # create sub array for anagrams
                answers.append([])

                # dd to real array
                # remove word from input array
                answers[index].append(strs.pop(0))

                # second pointer since i can go out of bounds
                start = 0

                # compare against all words in array
                for i in range(len(strs)):
                    # first check if len==
                    # if equal, remove from input array and add to answer array
                    if length == len(strs[start]) and makeDict(strs[start]) == dicky:
                        answers[index].append(strs.pop(start))

                    else:
                        start = start + 1
            else:
                break

        return answers
