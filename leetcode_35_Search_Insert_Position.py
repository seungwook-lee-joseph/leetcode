# 순서대로 숫자가 있다.
# 나는 특정 숫자 이상 큰 숫자에 포지션을 넣어야 한다.
# 중간 숫자는 정확하게 모른다.
# 위치만 찾아야 한다.

# 리스트 반을 나눈다.
# 리스트 값을 비교한다.
# 리스트 값이 특정 값 사이인지 체크한다.


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        len_nums = len(nums)
        half_position = int(len_nums/2)

        if target <= nums[0]:
            return 0
        elif nums[len_nums-1] < target:
            return len_nums 
        elif nums[len_nums-1] == target:
            return len_nums-1


        if target < nums[half_position]:
            return self.searchInsert(nums[:half_position],target)
        elif nums[half_position] <= target:
            return half_position + self.searchInsert(nums[half_position:],target)