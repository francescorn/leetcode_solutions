class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        else:
            prev = 1
            curr = 1
        for n in range(2, n+1):
            temp = curr
            curr = prev + curr
            prev = temp
        return curr
