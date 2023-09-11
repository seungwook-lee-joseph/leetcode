class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group = groupSizes
        result = []

        for i in group:
            mid_result = []
            for j in range(0,i):
                index = group.index(i)
                mid_result.append(index)
                group[index] = 0
            if i > 0:
                result.append(mid_result)
        
        return result