class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            if x < -2 ** 31:
                return 0
            x = abs(x)
            x = str(x)
            x = x[::-1]
            x = int(x)
            if x > 2 ** 31:
                return 0
            x = x * -1
            return x
        else:
            if x > 2 ** 31:
                return 0
            x = str(x)
            x = x[::-1]
            x = int(x)
            if x > 2 ** 31:
                return 0
            return x
