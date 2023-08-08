class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = x
        y = str(y)
        return y[::-1] == y
