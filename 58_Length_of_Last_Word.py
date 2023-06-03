class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        s_list = s.split()
        return len(s_list[-1])
