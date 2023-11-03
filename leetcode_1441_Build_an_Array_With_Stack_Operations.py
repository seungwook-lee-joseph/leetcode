class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        i = 1
        while i <= target[-1]:
            if i in target:
                result.append("Push")
            else :
                result.append("Push")
                result.append("Pop")
            i += 1
        return result        