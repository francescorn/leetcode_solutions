class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        num = str(num)
        num = num.rstrip("0")
        return num
