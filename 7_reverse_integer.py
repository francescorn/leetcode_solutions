class Solution:
    def reverse(self, x: int) -> int:
        y = abs(x)
        y = str(y)
        y = y[::-1]
        y = int(y)
        if y > 2 ** 31:
            return 0      
        elif x < 0:
            y = y * -1
            return y
        return y
