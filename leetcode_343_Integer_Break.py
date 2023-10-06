class Solution:
    @cache
    def integerBreak(self, n: int) -> int:
        if n <= 2:
            return 1
        
        maximum = 0 
        
        for i in range(2,n):
            x = i * self.integerBreak(n-i)
            y = i * (n-i)
            maximum = max(maximum, x, y)

        return maximum

