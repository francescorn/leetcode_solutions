class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        y = s.rstrip()
        return len(y.split()[-1])
