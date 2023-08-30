# find lowest length.
# match to the substr.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lengths = []
        for i in strs:
            lengths.append(len(i))

        minlen = min(lengths)

        result = ""

        for i in range(0,minlen):
            base = strs[0][0:minlen-i]
            if result == "":
                for s in strs:
                    if base == s[0:minlen-i]:
                        result = base
                    else:
                        base = ""
                        result = ""

        return result
                
            