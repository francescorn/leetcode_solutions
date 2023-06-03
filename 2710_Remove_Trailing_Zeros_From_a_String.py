class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        zero = "0"
        num = str(num)
        num = num.rstrip(zero)
        return num
