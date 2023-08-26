# integer to charlist
# charlist back order
# charlist to integer
# compare.


class Solution:
    def isPalindrome(self, x: int) -> bool:
        list = []
        if x < 0 :
            return False

        target = x
        counter = 0

        while x != 0:
            shared = x % 10
            x = int(x / 10)
            counter = counter * 10
            counter += shared

        if counter == target :
            return True
        else:
            return False