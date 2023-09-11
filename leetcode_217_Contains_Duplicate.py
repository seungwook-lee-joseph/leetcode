class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        set_nums = []

        for i in nums:
            if i in set_nums:
                return True
            else:
                set_nums.append(i)

        return False
# Over time limits.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
    
        while 0<len(nums):
            i = nums.pop()
            if i in nums:
                return True
        return False

# Over time limits.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        return len(set(nums)) != len(nums)
