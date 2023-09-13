# time limit
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        i = 0

        while i < n:                
            left = i-1
            right = i+1
            change = False
            if 0 <= left:
                if ratings[i] < ratings[left] \
                    and candies[left] <= candies[i]:
                    candies[left] = candies[i] + 1
                    change = True
            if right < n:
                if ratings[i] < ratings[right]\
                    and candies[right] <= candies[i]:
                    candies[right] = candies[i] + 1
                    change = True
            if change:
                if 0 < i:
                    i -= 1
            else:
                i += 1
        print(candies)
        return sum(candies)
    

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        i = 0

        for i in range(0,n-1):
            if ratings[i] < ratings[i+1]\
            and candies[i] >= candies[i+1]:
                candies[i+1] = candies[i] + 1

        for i in range(1,n):
            if ratings[n-i-1] > ratings[n-i]\
            and candies[n-i-1] <= candies[n-i]:
                candies[n-i-1] = candies[n-i] + 1



        return sum(candies)