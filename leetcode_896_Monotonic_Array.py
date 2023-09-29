_class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        len_nums = len(nums)
        result = True

        if nums[0] < nums[len(nums)-1]:
            for i in range(0, len_nums-1):
                if nums[i] > nums[i+1]:
                    result = False
        else:
            for i in range(0, len_nums-1):
                if nums[i] < nums[i+1]:
                    result = False


        return result 