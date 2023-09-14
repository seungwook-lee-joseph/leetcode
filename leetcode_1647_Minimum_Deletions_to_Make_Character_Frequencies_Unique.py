# 문자 별로 count를 해야하지 않을까?

class Solution:
    def minDeletions(self, s: str) -> int:
        dic= {}

        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        nums= []
        cnt = 0

        for i in dic:
            # How many chars.
            num = dic[i]
            # Case for duplicated
            while 0 < num:
                if num in nums:
                    cnt += 1    
                else:
                    nums.append(num)
                    break
                
                num -= 1 

        return cnt