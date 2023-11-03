# 숫자가 들어온다.
# 곱셈 조합을 만든다.
## [6, 3] [3, 6] [2, 3] [3, 2]
# 곱셈 조합에 하위 단어가 조합을 만들수 있는지 체크한다.
# 정렬의 경우를 계산한다.

class Solution:
    def set_of_bt(self, arr: List[int], target: int) -> List[List[int]]:
        return_set = []
        for i in arr:
            if target % i == 0:
                j = target / i
                if j in arr:
                    return_set.append([target, i, j])
        return return_set

    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        tot_length = len(arr)

        result_dict = dict()

        for a in range(0, tot_length):
            arr_sub = arr[:a]
            i = arr[a]

            arr_sub = arr.copy()  # Create a copy of arr to avoid modifying the original list.
            arr_sub.remove(i)
            result_dict[i] = 1
            set_bt = self.set_of_bt(arr_sub, i)
            for j in set_bt:

                semi_result = 1
                for k in j[1:]:
                    semi_result *= result_dict[k]          
                result_dict[i] += semi_result

        result = sum(result_dict.values()) % (10**9 + 7) # + len(arr)
        return result  # You should return the actual result here, not 0, once you calculate it.