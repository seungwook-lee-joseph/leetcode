
# make the dictionary
# bring the two characters
# comparing 1 and 2 
# if 1 > 2  -> add 1 -> next 1 is 2
# if 1 < 2  ->  add 2 - 1 -> next 1 is not 2 (over 2)


class Solution:
    def romanToInt(self, s: str) -> int:

        romandict = {
            'I': 1,
            'V': 5, 
            'X': 10, 
            'L': 50, 
            'C': 100, 
            'D': 500, 
            'M': 1000
            }
        
        s_len = len(s)-1
        i = 0
        result = 0

        while i <= s_len:
            if i == s_len:
                result += romandict[s[i]]
            else:
                a = romandict[s[i]]
                b = romandict[s[i+1]]
                if a >= b :
                    result += a
                else :
                    result += b
                    result -= a
                    i += 1
            i += 1

        return result